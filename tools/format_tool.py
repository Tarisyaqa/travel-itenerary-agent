# tools/format_tool.py
from google.adk.tools import tool

@tool
def validate_itinerary(itinerary) -> dict:
    errors = []
    normalized = []
    if not isinstance(itinerary, list):
        return {"ok": False, "errors": ["itinerary must be a list"], "itinerary": []}
    for idx, row in enumerate(itinerary):
        if not isinstance(row, dict):
            errors.append(f"row {idx} is not a dict")
            continue
        normalized.append({
            "day": row.get("day", ""),
            "time": row.get("time", ""),
            "activity": row.get("activity", ""),
            "location": row.get("location", ""),
            "maps_url": row.get("maps_url", ""),
            "booking_url": row.get("booking_url", ""),
            "cost": row.get("cost", ""),
            "notes": row.get("notes", "")
        })
    return {"ok": len(errors) == 0, "errors": errors, "itinerary": normalized}
