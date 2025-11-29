# agents/sub_agents/booking_agent.py
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

from tools.hotel_tool import search_hotels
from tools.transport_tool import search_transport
from tools.booking_tool import generate_hotel_booking_links, generate_transport_links

INSTRUCTION = (
    "BookingAgent: cari rekomendasi hotel & transport berdasarkan preferensi user. "
    "Gunakan tools yang tersedia (hotel DB, transport DB, booking link generator). "
    "Kembalikan daftar rekomendasi beserta link pemesanan dasar dan estimasi harga."
)

booking_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="booking_agent",
    description="Agent untuk rekomendasi hotel dan transport, dan pembuatan link booking.",
    instruction=INSTRUCTION,
    tools=[search_hotels, search_transport, generate_hotel_booking_links, generate_transport_links],
)
