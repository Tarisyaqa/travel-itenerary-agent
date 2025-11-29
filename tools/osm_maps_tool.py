# tools/osm_maps_tool.py
import requests
from google.adk.tools import tool

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OSRM_ROUTE_URL = "http://router.project-osrm.org/route/v1/driving"
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
HEADERS = {"User-Agent": "travel-itinerary-agent/1.0 (contact: your-email@example.com)"}

@tool
def nominatim_geocode(query: str, limit: int = 1) -> dict:
    params = {"q": query, "format": "json", "limit": limit, "addressdetails": 1}
    r = requests.get(NOMINATIM_URL, params=params, headers=HEADERS, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data

@tool
def osrm_route(origin_lat: float, origin_lon: float, dest_lat: float, dest_lon: float) -> dict:
    url = f"{OSRM_ROUTE_URL}/{origin_lon},{origin_lat};{dest_lon},{dest_lat}?overview=false"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

@tool
def overpass_search(keyword: str, lat: float, lon: float, radius: int = 2000) -> dict:
    q = f"""
    [out:json][timeout:25];
    (
      node["name"~"{keyword}", i](around:{radius},{lat},{lon});
      way["name"~"{keyword}", i](around:{radius},{lat},{lon});
      relation["name"~"{keyword}", i](around:{radius},{lat},{lon});
    );
    out center 20;
    """
    r = requests.post(OVERPASS_URL, data=q, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()
