RULES = [

# =====================================================
# GENERAL E-COMMERCE RULES (17)
# =====================================================
{
    "id": "EC-01",
    "title": "Seller name disclosure",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller"]
},
{
    "id": "EC-02",
    "title": "Seller contact details",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller_contact"]
},
{
    "id": "EC-03",
    "title": "Seller address disclosure",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller_address"]
},
{
    "id": "EC-04",
    "title": "Clear price display",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(b)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["price"]
},
{
    "id": "EC-05",
    "title": "All taxes/charges disclosure",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(c)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["charges"]
},
{
    "id": "EC-06",
    "title": "Return/Refund policy",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(d)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["returns"]
},
{
    "id": "EC-07",
    "title": "Delivery/Shipping details",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(e)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["delivery"]
},
{
    "id": "EC-08",
    "title": "Country of origin",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(f)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["origin"]
},
{
    "id": "EC-08-AMEND",
    "title": "Searchable Country of Origin Filter",
    "law": "Legal Metrology (Packaged Commodities) Amendment, 2025",
    "legal_reference": "Rule 6(11)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["origin_filter_enabled"]
},
{
    "id": "EC-09",
    "title": "Grievance officer details",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(4)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["grievance"]
},
{
    "id": "EC-10",
    "title": "Non-misleading description",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "EC-11",
    "title": "Non-manipulated reviews",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 5(3)(e)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["reviews"]
},
{
    "id": "EC-12",
    "title": "Clear product title",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["title"]
},
{
    "id": "EC-13",
    "title": "Brand/Manufacturer name",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "EC-14",
    "title": "Net quantity mention",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(1)(c)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["quantity"]
},
{
    "id": "EC-15",
    "title": "Product images provision",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["images"]
},
{
    "id": "EC-ENV-01",
    "title": "Plastic Packaging EPR Disclosure",
    "law": "Plastic Waste Management Rules, 2024",
    "legal_reference": "Rule 13(2)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["epr_registration_no"]
},

# =====================================================
# ELECTRONICS RULES (9)
# =====================================================
{
    "id": "EL-01",
    "title": "Warranty/Guarantee disclosure",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 5(3)(a)",
    "category": "electronics",
    "severity": "HIGH",
    "required_fields": ["warranty"]
},
{
    "id": "EL-02",
    "title": "Technical specifications",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(47)",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["specifications"]
},
{
    "id": "EL-03",
    "title": "Manufacturer disclosure",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["brand"]
},
{
    "id": "EL-04",
    "title": "Power/Voltage details",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["voltage"]
},
{
    "id": "EL-05",
    "title": "Safety instructions",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 10",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["safety"]
},
{
    "id": "EL-06",
    "title": "Energy rating (BEE)",
    "law": "Energy Conservation Act, 2001",
    "legal_reference": "BEE Regulations",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["energy_rating"]
},
{
    "id": "EL-07",
    "title": "Model number",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["model_number"]
},
{
    "id": "EL-08",
    "title": "Compatibility details",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(10)",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["compatibility"]
},
{
    "id": "EL-09",
    "title": "Mandatory BIS Mark",
    "law": "Bureau of Indian Standards Act, 2016",
    "legal_reference": "Section 14 / Scheme II",
    "category": "electronics",
    "severity": "HIGH",
    "required_fields": ["bis_standard_mark"]
},

# =====================================================
# FOOD RULES (11)
# =====================================================
{
    "id": "FD-01",
    "title": "Expiry date",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(4)",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["expiry"]
},
{
    "id": "FD-01-EXP",
    "title": "Minimum 45-day shelf life",
    "law": "FSSAI E-Commerce Guidelines, 2024",
    "legal_reference": "Advisory Clause 3",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["shelf_life_remaining"]
},
{
    "id": "FD-02",
    "title": "Ingredients list",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(1)",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["ingredients"]
},
{
    "id": "FD-03",
    "title": "FSSAI license number",
    "law": "Food Safety and Standards Act, 2006",
    "legal_reference": "Section 31",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["fssai"]
},
{
    "id": "FD-04",
    "title": "Allergen info",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(2)",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["allergen"]
},
{
    "id": "FD-05",
    "title": "Veg/Non-Veg symbol",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(4)(g)",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["veg_nonveg"]
},
{
    "id": "FD-06",
    "title": "Net weight",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(1)(c)",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["quantity"]
},
{
    "id": "FD-07",
    "title": "Storage instructions",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(10)",
    "category": "food",
    "severity": "LOW",
    "required_fields": ["storage"]
},
{
    "id": "FD-08",
    "title": "Manufacturer details",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(6)",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "FD-09",
    "title": "Nutritional info",
    "law": "FSS (Labelling and Display) Regulations, 2020",
    "legal_reference": "Rule 5(3)",
    "category": "food",
    "severity": "LOW",
    "required_fields": ["nutrition"]
},
{
    "id": "FD-10",
    "title": "No false health claims",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["description"]
},

# =====================================================
# HEALTH RULES (10)
# =====================================================
{
    "id": "HL-01",
    "title": "Medical disclaimer",
    "law": "Drugs & Magic Remedies Act, 1954",
    "legal_reference": "Section 3",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["disclaimer"]
},
{
    "id": "HL-02",
    "title": "Dosage instructions",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 96",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["dosage"]
},
{
    "id": "HL-03",
    "title": "No 100% cure claims",
    "law": "Drugs & Magic Remedies Act, 1954",
    "legal_reference": "Section 4",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["guaranteed"]
},
{
    "id": "HL-04",
    "title": "Non-misleading cure claims",
    "law": "Drugs & Magic Remedies Act, 1954",
    "legal_reference": "Section 5",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "HL-05",
    "title": "Manufacturer/Marketer details",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 96",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "HL-06",
    "title": "Intended use",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "HL-07",
    "title": "Warnings/Side effects",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Schedule H",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["warning"]
},
{
    "id": "HL-08",
    "title": "Age restriction",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 97",
    "category": "health",
    "severity": "LOW",
    "required_fields": ["age_limit"]
},
{
    "id": "HL-09",
    "title": "Prescription requirement",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Schedule H/H1",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["prescription_required"]
},
{
    "id": "HL-10",
    "title": "No misleading testimonials",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["reviews"]
},

# =====================================================
# CLOTHING RULES (7)
# =====================================================
{
    "id": "CL-01",
    "title": "Fabric composition",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["material"]
},
{
    "id": "CL-02",
    "title": "Size chart",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(47)",
    "category": "clothing",
    "severity": "HIGH",
    "required_fields": ["size"]
},
{
    "id": "CL-03",
    "title": "Wash care instructions",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 10",
    "category": "clothing",
    "severity": "LOW",
    "required_fields": ["care_instructions"]
},
{
    "id": "CL-04",
    "title": "Brand disclosure",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "clothing",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "CL-05",
    "title": "Country of origin",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(f)",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["origin"]
},
{
    "id": "CL-06",
    "title": "Return policy",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)(d)",
    "category": "clothing",
    "severity": "HIGH",
    "required_fields": ["returns"]
},
{
    "id": "CL-07",
    "title": "Accurate images",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["images"]
},

# =====================================================
# COSMETICS RULES (8)
# =====================================================
{
    "id": "CS-01",
    "title": "Full ingredients list",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 148",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["ingredients"]
},
{
    "id": "CS-02",
    "title": "Expiry date",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 148",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["expiry"]
},
{
    "id": "CS-03",
    "title": "Manufacturer details",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 148",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "CS-04",
    "title": "Usage instructions",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "CS-05",
    "title": "Warnings disclosure",
    "law": "Drugs and Cosmetics Act, 1940",
    "legal_reference": "Rule 150",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["warning"]
},
{
    "id": "CS-06",
    "title": "No false beauty claims",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "CS-07",
    "title": "Batch/Lot number",
    "law": "Drugs and Cosmetics Rules, 1945",
    "legal_reference": "Rule 96",
    "category": "cosmetics",
    "severity": "LOW",
    "required_fields": ["batch_no"]
},
{
    "id": "CS-08",
    "title": "Cruelty-free verification",
    "law": "Drugs and Cosmetics Rules (Amendment)",
    "legal_reference": "Rule 135-A",
    "category": "cosmetics",
    "severity": "LOW",
    "required_fields": ["cruelty_free_cert"]
},

# =====================================================
# TOYS RULES (6)
# =====================================================
{
    "id": "TY-01",
    "title": "Age appropriateness",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["age_limit"]
},
{
    "id": "TY-02",
    "title": "Safety warnings",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 10",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["warning"]
},
{
    "id": "TY-03",
    "title": "Choking hazard warning",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 10",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["choking_warning"]
},
{
    "id": "TY-04",
    "title": "Material safety",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "toys",
    "severity": "MEDIUM",
    "required_fields": ["material"]
},
{
    "id": "TY-05",
    "title": "Importer details",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "toys",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "TY-06",
    "title": "Accurate representation",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 2(28)",
    "category": "toys",
    "severity": "LOW",
    "required_fields": ["images"]
},

# =====================================================
# HOME APPLIANCES RULES (9)
# =====================================================
{
    "id": "AP-01",
    "title": "Energy rating (BEE)",
    "law": "Energy Conservation Act, 2001",
    "legal_reference": "BEE Regulations",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["energy_rating"]
},
{
    "id": "AP-01-QR",
    "title": "Mandatory QR Code for Energy Labels",
    "law": "BEE Regulations, 2025",
    "legal_reference": "Notification 2024/BEE",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["bee_qr_code"]
},
{
    "id": "AP-02",
    "title": "Warranty info",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 5(3)",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["warranty"]
},
{
    "id": "AP-03",
    "title": "Power/Voltage details",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["voltage"]
},
{
    "id": "AP-04",
    "title": "Usage instructions",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "AP-05",
    "title": "Safety warnings",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 10",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["safety"]
},
{
    "id": "AP-06",
    "title": "Brand disclosure",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "AP-07",
    "title": "Model number",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["model_number"]
},
{
    "id": "AP-08",
    "title": "BIS mark for heating range",
    "law": "Bureau of Indian Standards Act, 2016",
    "legal_reference": "QCO 2025",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["bis_mark"]
},

# =====================================================
# BOOKS RULES (10)
# =====================================================
{
    "id": "BK-01",
    "title": "ISBN disclosure",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18 (Right to Information)",
    "category": "books",
    "severity": "HIGH",
    "required_fields": ["isbn"]
},
{
    "id": "BK-02",
    "title": "Edition & Pub Year",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6",
    "category": "books",
    "severity": "MEDIUM",
    "required_fields": ["edition", "publication_year"]
},
{
    "id": "BK-03",
    "title": "Author & Publisher details",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(1)(a)",
    "category": "books",
    "severity": "MEDIUM",
    "required_fields": ["author", "publisher"]
},
{
    "id": "BK-04",
    "title": "Language specification",
    "law": "Consumer Protection (E-Commerce) Rules, 2020",
    "legal_reference": "Rule 4(2)",
    "category": "books",
    "severity": "LOW",
    "required_fields": ["language"]
},
{
    "id": "BK-05",
    "title": "Binding type",
    "law": "Consumer Protection Act, 2019",
    "legal_reference": "Section 18",
    "category": "books",
    "severity": "LOW",
    "required_fields": ["binding_type"]
},
{
    "id": "BK-06",
    "title": "Page count disclosure",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(1)(c)",
    "category": "books",
    "severity": "LOW",
    "required_fields": ["page_count"]
},
{
    "id": "BK-07",
    "title": "Front/Back cover images",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(10)",
    "category": "books",
    "severity": "HIGH",
    "required_fields": ["images"]
},
{
    "id": "BK-08",
    "title": "MRP clearly visible",
    "law": "Legal Metrology Act, 2009",
    "legal_reference": "Section 18",
    "category": "books",
    "severity": "HIGH",
    "required_fields": ["price"]
},
{
    "id": "BK-09",
    "title": "Generic Name 'Book' disclosure",
    "law": "Legal Metrology (Packaged Commodities) Rules, 2011",
    "legal_reference": "Rule 6(1)(b)",
    "category": "books",
    "severity": "LOW",
    "required_fields": ["title"]
},
{
    "id": "BK-10",
    "title": "Anti-Piracy/Originality Declaration",
    "law": "Copyright Act, 1957",
    "legal_reference": "Section 52-A",
    "category": "books",
    "severity": "MEDIUM",
    "required_fields": ["description"]
}
]