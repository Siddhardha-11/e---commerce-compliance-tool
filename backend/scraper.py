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
        # LimeRoad, Myntra, Ajio, etc.
        return _scrape_generic(url, html)




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
    """
    Extracts core product info from a Flipkart product page.
    Handles title, MRP, deal price, discount, seller, returns, and highlights.
    """
    soup = BeautifulSoup(html, "lxml")

    # ---------- TITLE ----------
    # Most Flipkart product pages use <span class="B_NuCI"> for title [web:23][web:24]
    title_el = (
        soup.select_one("span.B_NuCI")           # standard product title
        or soup.select_one('span[dir="auto"]')   # fallback
    )
    title = title_el.get_text(strip=True) if title_el else "No title found"

    # ---------- PRICE (MRP + DEAL + DISCOUNT) ----------
    mrp = None
    deal = None
    discount_text = None

    # Deal / selling price: <div class="_30jeq3 _16Jk6d">
    deal_el = soup.select_one("div._30jeq3._16Jk6d") or soup.select_one("div._30jeq3")
    if deal_el:
        deal_str = deal_el.get_text(strip=True)
        deal = _extract_price(deal_str)

    # MRP / original price: often in <div class="_3I9_wc _2p6lqe"> (striked) [web:23][web:24]
    mrp_el = soup.select_one("div._3I9_wc._2p6lqe")
    if mrp_el:
        mrp_str = mrp_el.get_text(strip=True)
        possible_mrp = _extract_price(mrp_str)
        if possible_mrp:
            mrp = possible_mrp

    # If only one price detected, treat it as both MRP and deal
    if mrp is None and deal is not None:
        mrp = deal
    if deal is None and mrp is not None:
        deal = mrp

    # Discount label like "18% off"
    discount_el = (
        soup.find("div", string=re.compile(r"\d+% off", re.I))
        or soup.find("span", string=re.compile(r"\d+% off", re.I))
    )
    if discount_el:
        discount_text = discount_el.get_text(strip=True)

    # If discount not shown but both mrp and deal differ, compute it
    if not discount_text and mrp and deal and mrp > deal:
        pct = round((mrp - deal) / mrp * 100)
        discount_text = f"{pct}% off"

    # ---------- SELLER ----------
    seller = "Unknown seller"
    # Look for a block labeled "Seller"
    seller_label = soup.find("span", string=re.compile(r"Seller", re.I))
    if seller_label:
        parent = seller_label.find_parent()
        if parent:
            seller_name_el = parent.find_next("span")
            if seller_name_el:
                seller = seller_name_el.get_text(strip=True)

    # ---------- RETURNS POLICY ----------
    returns = None
    returns_candidate = None
    # Examples: "7 days Replacement", "10 days Returnable"
    for node in soup.select("span, div, li"):
        txt = node.get_text(strip=True)
        if re.search(r"\b\d+\s*day[s]?\s+(Replacement|Returnable)", txt, re.I):
            returns_candidate = txt
            break
    if returns_candidate:
        returns = returns_candidate[:120]

    # ---------- SHORT DESCRIPTION / HIGHLIGHTS ----------
    description = None
    highlights = soup.select("li._21Ahn-")  # common highlights list
    if highlights:
        items = [li.get_text(" ", strip=True) for li in highlights]
        description = " | ".join(items)[:200]
    else:
        full_text = soup.get_text(separator=" ", strip=True)
        description = full_text[:200] if full_text else None

    # ---------- BUILD PRODUCT DATA ----------
    return ProductData(
        url=url,
        title=title[:150],
        seller=seller,
        price=Price(
            mrp=mrp,
            deal=deal,
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

    # 1) MRP / crossed price
    mrp_block = soup.select_one("span.a-price.a-text-price")
    if mrp_block:
        mrp_whole = mrp_block.select_one("span.a-price-whole")
        mrp_frac = mrp_block.select_one("span.a-price-fraction")
        if mrp_whole:
            mrp_str = mrp_whole.text.replace(",", "").strip()
            if mrp_frac:
                mrp_str = f"{mrp_str}.{mrp_frac.text.strip()}"
            mrp_price = _safe_float(mrp_str)

    # 2) Deal price
    deal_block = None
    for block in soup.select("span.a-price"):
        classes = block.get("class", [])
        if "a-text-price" not in classes:
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

    # 1)Amazon technical details / product details tables
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
        # 2)"Technical Details" / "Product Details"
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


def _scrape_generic(url: str, html: str) -> ProductData:
    soup = BeautifulSoup(html, "lxml")

    # ---------- TITLE ----------
    title = None
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()

    if not title and soup.title and soup.title.string:
        title = soup.title.string.strip()

    if not title:
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)

    if not title:
        title = "No title found"

    # ---------- PRICE ----------
    mrp = None
    deal = None
    discount_text = None

    # Try explicit “Buy this at ₹1299” / “₹1999 51% off” patterns common on LimeRoad [web:37][web:38]
    full_text = soup.get_text(separator=" ", strip=True)

    # First price as deal
    deal = _extract_price(full_text)
    mrp = deal

    # Try to capture a second, higher price as MRP (if present)
    prices = re.findall(r"₹\s*([\d,]+(?:\.\d+)?)", full_text)
    if len(prices) >= 2:
        nums = [ _safe_float(p.replace(",", "")) for p in prices ]
        nums = [n for n in nums if n is not None]
        if len(nums) >= 2:
            high = max(nums)
            low = min(nums)
            mrp, deal = high, low

    # Discount like "20% OFF" or "51% off" [web:37][web:38]
    m = re.search(r"(\d+)%\s*off", full_text, re.I)
    if m:
        discount_text = f"{m.group(1)}% off"

    # Compute discount if not found but both prices differ
    if not discount_text and mrp and deal and mrp > deal:
        pct = round((mrp - deal) / mrp * 100)
        discount_text = f"{pct}% off"

    # ---------- SELLER ----------
    seller = "Unknown seller"
    seller_label = soup.find(string=re.compile(r"Brand|Seller|Sold by", re.I))
    if seller_label:
        parent = seller_label.find_parent()
        if parent:
            cand = parent.find_next(["strong", "span", "div"])
            if cand:
                seller = cand.get_text(strip=True)

    # ---------- RETURNS ----------
    returns = None
    for node in soup.select("span, div, li"):
        txt = node.get_text(strip=True)
        if re.search(r"\b\d+\s*day[s]?\s+(return|refund|replacement|returnable)", txt, re.I):
            returns = txt[:120]
            break

    # ---------- DESCRIPTION ----------
    description = None

    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        description = meta_desc["content"].strip()

    if not description:
        desc_div = (
            soup.find("div", id=re.compile(r"productDescription|description", re.I))
            or soup.find("div", class_=re.compile(r"description|prod-desc|product-info", re.I))
        )
        if desc_div:
            description = desc_div.get_text(" ", strip=True)

    if not description:
        for p in soup.find_all("p"):
            txt = p.get_text(" ", strip=True)
            if len(txt) > 50:
                description = txt
                break

    if not description and full_text:
        description = full_text

    if description:
        description = description[:400]

    return ProductData(
        url=url,
        title=title[:150],
        seller=seller,
        price=Price(
            mrp=mrp,
            deal=deal,
            discount=discount_text
        ),
        returns=returns,
        description=description,
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
        "https://amzn.in/d/aKD12Yo",
        "https://amzn.in/d/2sgbIfs"
    ]
    for u in test_urls:
        try:
            print(f"\nTesting {u}")
            p = scrape_product(u)
            print(p.model_dump_json(indent=2))
        except Exception as e:
            print(f"Error for {u}: {e}")
