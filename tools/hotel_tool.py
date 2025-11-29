# tools/hotel_tool.py
from google.adk.tools import tool

HOTEL_DB = [
    {"name": "Hotel Harmoni Puncak", "price": 550000, "rating": 4.3, "location": "Puncak, Bogor", "booking_url": "https://www.booking.com/hotel-harmoni"},
    {"name": "Green Forest Resort", "price": 800000, "rating": 4.7, "location": "Cisarua, Puncak", "booking_url": "https://www.agoda.com/green-forest"},
]

@tool
def search_hotels(location: str, max_price: int = None):
    filtered = []
    for h in HOTEL_DB:
        if location.lower() in h["location"].lower():
            if max_price is None or h["price"] <= max_price:
                filtered.append(h)
    return filtered
