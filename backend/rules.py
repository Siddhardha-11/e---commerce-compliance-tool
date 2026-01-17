RULES = [

# =====================================================
# GENERAL E-COMMERCE RULES (17)
# =====================================================

{
    "id": "EC-01",
    "title": "Seller name must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller"]
},
{
    "id": "EC-02",
    "title": "Seller contact details must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller_contact"]
},
{
    "id": "EC-03",
    "title": "Seller address must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(a)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["seller_address"]
},
{
    "id": "EC-04",
    "title": "Product price must be clearly displayed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(b)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["price"]
},
{
    "id": "EC-05",
    "title": "All taxes and charges must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(c)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["charges"]
},
{
    "id": "EC-06",
    "title": "Return and refund policy must be available",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(d)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["returns"]
},
{
    "id": "EC-07",
    "title": "Delivery and shipping details must be provided",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(e)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["delivery"]
},
{
    "id": "EC-08",
    "title": "Country of origin must be mentioned",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(f)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["origin"]
},
{
    "id": "EC-08-AMEND",
    "title": "Searchable Country of Origin Filter for Imported Goods",
    "law": "Legal Metrology (Packaged Commodities) 2nd Amendment, 2025",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["origin_filter_enabled"]
},
{
    "id": "EC-09",
    "title": "Grievance officer details must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(5)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["grievance"]
},
{
    "id": "EC-10",
    "title": "Product description must not be misleading",
    "law": "Consumer Protection Act 2019 – Section 2(28)",
    "category": "all",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "EC-11",
    "title": "Ratings and reviews must not be manipulated",
    "law": "E-Commerce Rules 2020 – Rule 5(3)",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["reviews"]
},
{
    "id": "EC-12",
    "title": "Product title must be clearly mentioned",
    "law": "Consumer Protection Act 2019",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["title"]
},
{
    "id": "EC-13",
    "title": "Brand or manufacturer name must be disclosed",
    "law": "Legal Metrology Act",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "EC-14",
    "title": "Net quantity must be mentioned",
    "law": "Legal Metrology Rules",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["quantity"]
},
{
    "id": "EC-15",
    "title": "Product images must be provided",
    "law": "Consumer Protection Act 2019",
    "category": "all",
    "severity": "LOW",
    "required_fields": ["images"]
},
{
    "id": "EC-ENV-01",
    "title": "Plastic Packaging EPR Disclosure",
    "law": "Plastic Waste Management (Amendment) Rules, 2024",
    "category": "all",
    "severity": "MEDIUM",
    "required_fields": ["epr_registration_no", "plastic_type_label"]
},

# =====================================================
# ELECTRONICS RULES (9)
# =====================================================

{
    "id": "EL-01",
    "title": "Warranty or guarantee must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 5(3)",
    "category": "electronics",
    "severity": "HIGH",
    "required_fields": ["warranty"]
},
{
    "id": "EL-02",
    "title": "Technical specifications must be provided",
    "law": "Consumer Protection Act 2019",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["specifications"]
},
{
    "id": "EL-03",
    "title": "Brand or manufacturer must be disclosed",
    "law": "Legal Metrology Act",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["brand"]
},
{
    "id": "EL-04",
    "title": "Power rating or voltage details must be mentioned",
    "law": "Legal Metrology Rules",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["voltage"]
},
{
    "id": "EL-05",
    "title": "Safety instructions or warnings must be provided",
    "law": "Consumer Protection Act 2019",
    "category": "electronics",
    "severity": "MEDIUM",
    "required_fields": ["safety"]
},
{
    "id": "EL-06",
    "title": "Energy efficiency rating must be disclosed if applicable",
    "law": "BEE Guidelines",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["energy_rating"]
},
{
    "id": "EL-07",
    "title": "Model number must be disclosed",
    "law": "Consumer Protection Act 2019",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["model_number"]
},
{
    "id": "EL-08",
    "title": "Compatibility details must be provided",
    "law": "Consumer Protection Act 2019",
    "category": "electronics",
    "severity": "LOW",
    "required_fields": ["compatibility"]
},
{
    "id": "EL-09",
    "title": "Mandatory BIS for Household Appliances (Kettles/HairTools/Massagers)",
    "law": "BIS Household Appliances QCO, 2025",
    "category": "electronics",
    "severity": "HIGH",
    "required_fields": ["bis_standard_mark"]
},

# =====================================================
# FOOD RULES (11)
# =====================================================

{
    "id": "FD-01",
    "title": "Expiry or best-before date must be mentioned",
    "law": "FSSAI Labelling Regulations",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["expiry"]
},
{
    "id": "FD-01-EXP",
    "title": "Minimum 45-day shelf life at delivery",
    "law": "FSSAI Advisory (Dec 2024)",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["shelf_life_remaining"]
},
{
    "id": "FD-02",
    "title": "Ingredients list must be disclosed",
    "law": "FSSAI Labelling Regulations",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["ingredients"]
},
{
    "id": "FD-03",
    "title": "FSSAI license number must be displayed",
    "law": "FSSAI Act, 2006",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["fssai"]
},
{
    "id": "FD-04",
    "title": "Allergen information must be disclosed",
    "law": "FSSAI Regulations",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["allergen"]
},
{
    "id": "FD-05",
    "title": "Vegetarian or non-vegetarian symbol must be shown",
    "law": "FSSAI Regulations",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["veg_nonveg"]
},
{
    "id": "FD-06",
    "title": "Net quantity or weight must be mentioned",
    "law": "Legal Metrology Rules",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["quantity"]
},
{
    "id": "FD-07",
    "title": "Storage instructions must be mentioned",
    "law": "FSSAI Regulations",
    "category": "food",
    "severity": "LOW",
    "required_fields": ["storage"]
},
{
    "id": "FD-08",
    "title": "Manufacturer or packer details must be disclosed",
    "law": "FSSAI Regulations",
    "category": "food",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "FD-09",
    "title": "Nutritional information must be provided",
    "law": "FSSAI Regulations",
    "category": "food",
    "severity": "LOW",
    "required_fields": ["nutrition"]
},
{
    "id": "FD-10",
    "title": "No false health claims allowed on food products",
    "law": "Consumer Protection Act 2019",
    "category": "food",
    "severity": "HIGH",
    "required_fields": ["description"]
},

# =====================================================
# HEALTH RULES (10)
# =====================================================

{
    "id": "HL-01",
    "title": "Medical disclaimer must be present",
    "law": "Drugs & Magic Remedies Act, 1954",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["disclaimer"]
},
{
    "id": "HL-02",
    "title": "Dosage or usage instructions must be provided",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["dosage"]
},
{
    "id": "HL-03",
    "title": "Guaranteed cure or 100% result claims are prohibited",
    "law": "Drugs & Magic Remedies Act, 1954",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["guaranteed", "100%"]
},
{
    "id": "HL-04",
    "title": "Disease cure or prevention claims must not be misleading",
    "law": "Drugs & Magic Remedies Act, 1954",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "HL-05",
    "title": "Manufacturer or marketer details must be disclosed",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "HL-06",
    "title": "Intended use or purpose must be mentioned",
    "law": "Consumer Protection Act 2019",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "HL-07",
    "title": "Warnings or side effects must be disclosed",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "health",
    "severity": "MEDIUM",
    "required_fields": ["warning"]
},
{
    "id": "HL-08",
    "title": "Age restriction must be disclosed where applicable",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "health",
    "severity": "LOW",
    "required_fields": ["age_limit"]
},
{
    "id": "HL-09",
    "title": "Prescription-only products must indicate prescription requirement",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["prescription_required"]
},
{
    "id": "HL-10",
    "title": "Misleading medical testimonials are prohibited",
    "law": "Consumer Protection Act 2019 – Section 2(28)",
    "category": "health",
    "severity": "HIGH",
    "required_fields": ["reviews"]
},

# =====================================================
# CLOTHING / FASHION RULES (7)
# =====================================================

{
    "id": "CL-01",
    "title": "Fabric or material composition must be disclosed",
    "law": "Consumer Protection Act, 2019",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["material"]
},
{
    "id": "CL-02",
    "title": "Size information or size chart must be provided",
    "law": "Consumer Protection Act, 2019",
    "category": "clothing",
    "severity": "HIGH",
    "required_fields": ["size"]
},
{
    "id": "CL-03",
    "title": "Care and wash instructions must be mentioned",
    "law": "Consumer Protection Act, 2019",
    "category": "clothing",
    "severity": "LOW",
    "required_fields": ["care_instructions"]
},
{
    "id": "CL-04",
    "title": "Brand or manufacturer name must be disclosed",
    "law": "Legal Metrology Rules",
    "category": "clothing",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "CL-05",
    "title": "Country of origin must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(f)",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["origin"]
},
{
    "id": "CL-06",
    "title": "Return and exchange policy must be clearly stated",
    "law": "E-Commerce Rules 2020 – Rule 4(2)(d)",
    "category": "clothing",
    "severity": "HIGH",
    "required_fields": ["returns"]
},
{
    "id": "CL-07",
    "title": "Product images must accurately represent the item",
    "law": "Consumer Protection Act, 2019",
    "category": "clothing",
    "severity": "MEDIUM",
    "required_fields": ["images"]
},

# =====================================================
# COSMETICS / PERSONAL CARE RULES (8)
# =====================================================

{
    "id": "CS-01",
    "title": "Complete ingredient list must be disclosed",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["ingredients"]
},
{
    "id": "CS-02",
    "title": "Expiry or best-before date must be mentioned",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["expiry"]
},
{
    "id": "CS-03",
    "title": "Manufacturer or marketer details must be disclosed",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "CS-04",
    "title": "Usage instructions must be provided",
    "law": "Consumer Protection Act, 2019",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "CS-05",
    "title": "Warnings or precautions must be disclosed",
    "law": "Drugs & Cosmetics Act, 1940",
    "category": "cosmetics",
    "severity": "MEDIUM",
    "required_fields": ["warning"]
},
{
    "id": "CS-06",
    "title": "False, permanent, or guaranteed beauty claims are prohibited",
    "law": "Consumer Protection Act, 2019",
    "category": "cosmetics",
    "severity": "HIGH",
    "required_fields": ["description"]
},
{
    "id": "CS-07",
    "title": "Batch or lot number must be mentioned",
    "law": "Drugs & Cosmetics Rules",
    "category": "cosmetics",
    "severity": "LOW",
    "required_fields": ["batch_no"]
},
{
    "id": "CS-08",
    "title": "Cruelty-free or Animal Testing Claims Verification",
    "law": "Drugs & Cosmetics Rules (Amended)",
    "category": "cosmetics",
    "severity": "LOW",
    "required_fields": ["cruelty_free_cert"]
},

# =====================================================
# TOYS & BABY PRODUCTS RULES (6)
# =====================================================

{
    "id": "TY-01",
    "title": "Age appropriateness must be clearly specified",
    "law": "Consumer Protection Act, 2019",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["age_limit"]
},
{
    "id": "TY-02",
    "title": "Safety warnings must be disclosed",
    "law": "Consumer Protection Act, 2019",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["warning"]
},
{
    "id": "TY-03",
    "title": "Choking or small-parts warning must be disclosed",
    "law": "Consumer Protection Act, 2019",
    "category": "toys",
    "severity": "HIGH",
    "required_fields": ["choking_warning"]
},
{
    "id": "TY-04",
    "title": "Material safety or non-toxic claim must be disclosed if applicable",
    "law": "Consumer Protection Act, 2019",
    "category": "toys",
    "severity": "MEDIUM",
    "required_fields": ["material"]
},
{
    "id": "TY-05",
    "title": "Manufacturer or importer details must be provided",
    "law": "Legal Metrology Rules",
    "category": "toys",
    "severity": "MEDIUM",
    "required_fields": ["manufacturer"]
},
{
    "id": "TY-06",
    "title": "Product images must accurately reflect the toy",
    "law": "Consumer Protection Act, 2019",
    "category": "toys",
    "severity": "LOW",
    "required_fields": ["images"]
},

# =====================================================
# HOME APPLIANCES RULES (12)
# =====================================================

{
    "id": "AP-01",
    "title": "Energy efficiency rating must be disclosed if applicable",
    "law": "Bureau of Energy Efficiency (BEE) Guidelines",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["energy_rating"]
},
{
    "id": "AP-01-QR",
    "title": "Mandatory QR Code for Energy Labels",
    "law": "BEE (Appliance Labelling) Regulations, 2025",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["bee_qr_code"]
},
{
    "id": "AP-02",
    "title": "Warranty or guarantee information must be disclosed",
    "law": "E-Commerce Rules 2020 – Rule 5(3)",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["warranty"]
},
{
    "id": "AP-03",
    "title": "Power consumption or voltage details must be provided",
    "law": "Legal Metrology Rules",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["voltage"]
},
{
    "id": "AP-04",
    "title": "Usage or installation instructions must be mentioned",
    "law": "Consumer Protection Act, 2019",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["usage"]
},
{
    "id": "AP-05",
    "title": "Safety warnings must be disclosed",
    "law": "Consumer Protection Act, 2019",
    "category": "appliances",
    "severity": "MEDIUM",
    "required_fields": ["safety"]
},
{
    "id": "AP-06",
    "title": "Brand or manufacturer details must be disclosed",
    "law": "Legal Metrology Rules",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["brand"]
},
{
    "id": "AP-07",
    "title": "Model number must be disclosed",
    "law": "Consumer Protection Act, 2019",
    "category": "appliances",
    "severity": "LOW",
    "required_fields": ["model_number"]
},
{
    "id": "AP-08",
    "title": "Mandatory BIS mark for Liquid Heating/Cooking range",
    "law": "BIS (Household Appliances) QCO, 2025",
    "category": "appliances",
    "severity": "HIGH",
    "required_fields": ["bis_mark"]
}

]