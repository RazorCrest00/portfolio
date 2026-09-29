# CODE_RUNNER: 3.05 Homework - SFI backend validator
def validate_record(part, existing_spec_numbers, valid_categories):
    has_name = bool(part.get("product_name", "").strip())
    has_spec = bool(part.get("spec_number", "").strip())
    has_date = bool(part.get("effective_date", "").strip())
    category_ok = part.get("category") in valid_categories
    duplicate_spec = part.get("spec_number", "").strip() in existing_spec_numbers
    return has_name and has_spec and has_date and category_ok and not duplicate_spec

existing_spec_numbers = ["1.1", "2.1"]
valid_categories = ["Auto Racing", "Drag Racing"]
test_records = [
    {"product_name": "Multiple Disc Clutch Assemblies", "category": "Auto Racing", "spec_number": "1.2", "effective_date": "Feb. 9, 2006"},
    {"product_name": "Replacement Flywheels", "category": "Street Car", "spec_number": "3.1", "effective_date": "Jan. 1, 2026"},
    {"product_name": "Existing Flywheel Record", "category": "Drag Racing", "spec_number": "1.1", "effective_date": "Jan. 1, 2026"},
]
for candidate in test_records:
    valid = validate_record(candidate, existing_spec_numbers, valid_categories)
    if valid:
        print(candidate["spec_number"] + ": ACCEPTED")
    else:
        print(candidate["spec_number"] + ": REJECTED")
