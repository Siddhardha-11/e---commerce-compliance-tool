import time
import random
import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from models import ProductData, Price

ua = UserAgent()


def scrape_product(url: str) -> ProductData:

    domain = urlparse(url).netloc.lower()

    html = _fetch_html(url)

    if "flipkart.com" in domain:
        return _scrape_flipkart(url, html)
    elif "amazon.in" in domain or "amazon.com" in domain or "amzn.in" in domain:
        return _scrape_amazon(url, html)
    else:
        raise ValueError(f"Unsupported domain: {domain}")



def _fetch_html(url: str) -> str:

    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-IN,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    time.sleep(random.uniform(1, 2))

    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.text


def _scrape_flipkart(url: str, html: str) -> ProductData:

    soup = BeautifulSoup(html, "lxml")

    # Title (update selector after inspecting)
    title_el = soup.select_one('span[dir="auto"]') or soup.select_one("._2WkVRV")
    title = title_el.text.strip() if title_el else "No title found"

    # Price
    price_el = soup.select_one('[data-testid="price"]') or soup.select_one("._30jeqT")
    price_text = price_el.text.strip() if price_el else ""
    # Extract first ₹number pattern
    mrp = _extract_price(price_text)

    # Discount text
    discount_match = re.search(r"(\d+)%\s*off", price_text)
    discount = f"{discount_match.group(1)}% off" if discount_match else None

    # Seller
    seller_el = soup.select_one('a[href*="/seller"]') or soup.select_one(".sellerName")
    seller = seller_el.text.strip() if seller_el else "Unknown seller"

    # Returns / refund policy (very rough)
    returns_el = soup.find(string=re.compile(r"return|refund", re.I))
    returns = returns_el.strip()[:120] if returns_el else None

    # Short description
    full_text = soup.get_text(separator=" ", strip=True)
    description = full_text[:200] if full_text else None

    return ProductData(
        url=url,
        title=title[:150],
        seller=seller,
            price=Price(
        mrp=mrp_price,
        deal=deal_price,
        discount=discount_text
    ),

        returns=returns,
        description=description,
    )


def _scrape_amazon(url: str, html: str) -> ProductData:
    soup = BeautifulSoup(html, "lxml")

    # Title
    title_el = soup.select_one("#productTitle") or soup.select_one("h1 span")
    title = title_el.text.strip() if title_el else "No title found"


    # -------- PRICE BLOCK (DEAL + MRP) --------

    mrp_price = None
    deal_price = None

    # 1) MRP / crossed price: span.a-price.a-text-price (this is usually struck-through)
    mrp_block = soup.select_one("span.a-price.a-text-price")
    if mrp_block:
        mrp_whole = mrp_block.select_one("span.a-price-whole")
        mrp_frac = mrp_block.select_one("span.a-price-fraction")
        if mrp_whole:
            mrp_str = mrp_whole.text.replace(",", "").strip()
            if mrp_frac:
                mrp_str = f"{mrp_str}.{mrp_frac.text.strip()}"
            mrp_price = _safe_float(mrp_str)

    # 2) Deal price: first a-price that is NOT a-text-price (bold current price)
    deal_block = None
    for block in soup.select("span.a-price"):
        classes = block.get("class", [])
        if "a-text-price" not in classes:  # skip crossed MRP blocks
            deal_block = block
            break

    if deal_block:
        whole = deal_block.select_one("span.a-price-whole")
        frac = deal_block.select_one("span.a-price-fraction")
        if whole:
            deal_str = whole.text.replace(",", "").strip()
            if frac:
                deal_str = f"{deal_str}.{frac.text.strip()}"
            deal_price = _safe_float(deal_str)

    # 3) Fallback: if nothing found, try generic ₹n,nnn pattern
    if not mrp_price and not deal_price:
        text = soup.get_text(separator=" ", strip=True)
        generic_price = _extract_price(text)
        if generic_price:
            deal_price = generic_price

    # Discount:
    # 1) If Amazon shows explicit "18% off", read it.
    discount_text = None
    explicit_span = soup.find("span", string=re.compile(r"-?\d+%(\s*off)?", re.I))
    if explicit_span:
        discount_text = explicit_span.get_text(strip=True)

    # 2) If not shown, but mrp and deal both exist, compute it.
    if not discount_text and mrp_price and deal_price and mrp_price > deal_price:
        pct = round((mrp_price - deal_price) / mrp_price * 100)
        discount_text = f"{pct}% off"


    # Seller
    seller_el = soup.select_one("#sellerProfileTriggerId")
    seller = seller_el.text.strip() if seller_el else "Amazon"

    # RETURNS LOGIC
    returns = None

    #returns / refund
    returns_container = soup.find(
        id=re.compile(r"RETURNS_POLICY|RETURNS-FEATURE", re.I)
    ) or soup.find("div", string=re.compile(r"Returns", re.I))

    if returns_container:
        returns_text = returns_container.get_text(separator=" ", strip=True)
        returns = returns_text[:120]
    else:
        #10 days returnable
        for node in soup.select("span, li, div"):
            txt = node.get_text(strip=True)
            if re.search(r"\b\d+\s*-?\s*day[s]?\s+return", txt, re.I):
                returns = txt[:120]
                break
    
        technical_details = None

    # 1) Try Amazon technical details / product details tables
    tech_table = soup.find(
        "table",
        id=re.compile(r"productDetails_techSpec|productDetails_detailBullets", re.I)
    )

    rows = []
    if tech_table:
        for row in tech_table.select("tr"):
            cells = row.find_all(["th", "td"])
            if len(cells) >= 2:
                key = cells[0].get_text(" ", strip=True)
                val = cells[1].get_text(" ", strip=True)
                rows.append(f"{key}: {val}")

    if rows:
        technical_details = " | ".join(rows)
    else:
        # 2) Fallback: section under heading "Technical Details" / "Product Details"
        heading = soup.find(
            lambda tag: tag.name in ["h1", "h2", "h3", "span"]
            and re.search(r"Technical Details|Product Details", tag.get_text(), re.I)
        )
        if heading:
            container = heading.find_parent()
            next_table = container.find_next("table")
            if next_table:
                rows = []
                for row in next_table.select("tr"):
                    cells = row.find_all(["th", "td"])
                    if len(cells) >= 2:
                        key = cells[0].get_text(" ", strip=True)
                        val = cells[1].get_text(" ", strip=True)
                        rows.append(f"{key}: {val}")
                if rows:
                    technical_details = " | ".join(rows)


    # Description
    full_text = soup.get_text(separator=" ", strip=True)
    description = full_text[:200] if full_text else None

    return ProductData(
        url=url,
        title=title[:150],
        seller=seller,
        price=Price(
            mrp=mrp_price or deal_price,
            deal=deal_price or mrp_price,
            discount=discount_text
        ),
        returns=returns,
        technical_details=technical_details,
    )




def _extract_price(text: str):
    """
    Finds first ₹number in text and returns it as float.
    """
    match = re.search(r"₹\s*([\d,]+(?:\.\d+)?)", text)
    if not match:
        return None
    return _safe_float(match.group(1).replace(",", ""))


def _safe_float(value: str):
    try:
        return float(value)
    except Exception:
        return None


if __name__ == "__main__":

    test_urls = [
        "https://amzn.in/d/3db7ueq",
        "https://amzn.in/d/2sgbIfs"
    ]
    for u in test_urls:
        try:
            print(f"\nTesting {u}")
            p = scrape_product(u)
            print(p.model_dump_json(indent=2))
        except Exception as e:
            print(f"Error for {u}: {e}")
