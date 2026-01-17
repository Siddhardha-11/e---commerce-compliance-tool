from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from io import BytesIO

def generate_pdf_report(result: dict) -> BytesIO:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "SafeBuy Compliance Report")
    y -= 30

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Generated on: {datetime.utcnow().strftime('%d %b %Y %H:%M UTC')}")
    y -= 40

    product = result["product"]

    # Product details
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Product Details")
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Title: {product.get('title')}")
    y -= 15
    c.drawString(50, y, f"Seller: {product.get('seller', 'Unknown')}")
    y -= 15
    c.drawString(50, y, f"URL: {product.get('url')}")
    y -= 25

    # Risk score
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, f"Risk Score: {result['risk_score']}")
    y -= 25

    # Violations
    c.drawString(50, y, "Violations")
    y -= 20

    c.setFont("Helvetica", 10)
    violations = result.get("violations", [])

    if not violations:
        c.drawString(60, y, "No violations detected.")
    else:
        for v in violations:
            if y < 80:
                c.showPage()
                y = height - 50

            c.drawString(60, y, f"- {v['description']} ({v['severity']})")
            y -= 14

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
