# agents/sub_agents/format_agent.py
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

from tools.format_tool import validate_itinerary

INSTRUCTION = (
    "FormatAgent: merapikan dan menormalisasi itinerary dari berbagai sumber. "
    "Pastikan struktur konsisten (list of dict) dan bahasa Indonesia."
)

format_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="format_agent",
    description="Agent untuk validasi dan formatting itinerary.",
    instruction=INSTRUCTION,
    tools=[validate_itinerary],
)
