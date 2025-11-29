# tools/transport_tool.py
from google.adk.tools import tool

TRANSPORT_DB = [
    {"type": "Kereta", "route": "Jakarta → Bogor", "price": 20000, "booking_url": "https://tiket.com/kereta"},
    {"type": "Travel", "route": "Jakarta → Puncak", "price": 150000, "booking_url": "https://traveloka.com/travel"},
]

@tool
def search_transport(origin: str, destination: str):
    results = []
    for t in TRANSPORT_DB:
        if origin.lower() in t["route"].lower() and destination.lower() in t["route"].lower():
            results.append(t)
    return results
