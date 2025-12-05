"""Data validation utilities to ensure input JSON has required fields."""

REQUIRED_FIELDS = ["link", "headline", "category", "short_description", "date"]

def validate_record(rec: dict) -> bool:
    return all(field in rec for field in REQUIRED_FIELDS)
