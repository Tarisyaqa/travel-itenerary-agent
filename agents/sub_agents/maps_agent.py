# agents/sub_agents/maps_agent.py
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

# Import tools (google and osm fallback)
from tools.google_maps_tool import places_search as google_places_search
from tools.google_maps_tool import distance_matrix as google_distance_matrix
from tools.google_maps_tool import geocode as google_geocode

from tools.osm_maps_tool import nominatim_geocode, osrm_route, overpass_search

INSTRUCTION = (
    "MapsAgent: gunakan tools yang tersedia untuk mencari lokasi, mengonversi alamat↔koordinat, "
    "menghitung jarak/durasi, dan mencari tempat (hotel, atraksi, restoran). "
    "Jika Google Maps API tersedia, gunakan google_* tools. Jika tidak, fallback ke OSM tools. "
    "Jawaban dalam Bahasa Indonesia."
)

maps_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="maps_agent",
    description="Agent untuk geocoding, routing, dan place search (Google Maps + OSM fallback).",
    instruction=INSTRUCTION,
    tools=[
        # Google tools (may raise if API key missing at runtime)
        google_places_search,
        google_distance_matrix,
        google_geocode,
        # OSM fallback tools
        nominatim_geocode,
        osrm_route,
        overpass_search,
    ],
)
