# tools/booking_tool.py
import urllib.parse
from google.adk.tools import tool

@tool
def generate_hotel_booking_links(hotel_name: str, city: str) -> dict:
    q = urllib.parse.quote_plus(f"{hotel_name} {city}")
    return {
        "booking_com": f"https://www.booking.com/searchresults.html?ss={q}",
        "agoda": f"https://www.agoda.com/search?searchTerm={q}",
        "traveloka": f"https://www.traveloka.com/en-en/hotel/search?keyword={q}"
    }

@tool
def generate_transport_links(origin: str, destination: str, date: str = "") -> dict:
    orig = urllib.parse.quote_plus(origin)
    dest = urllib.parse.quote_plus(destination)
    return {
        "traveloka_flight": f"https://www.traveloka.com/en-id/flights?origin={orig}&destination={dest}",
        "google_maps_directions": f"https://www.google.com/maps/dir/?api=1&origin={orig}&destination={dest}"
    }
