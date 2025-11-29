# agents/sub_agents/excel_agent.py
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

from tools.excel_tool import generate_excel_itinerary

INSTRUCTION = (
    "ExcelAgent: ketika diminta membuat file Excel, panggil tool generate_excel_itinerary "
    "dengan daftar itinerary terstruktur (list of dict). Kembalikan path file yang dibuat."
)

excel_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="excel_agent",
    description="Agent untuk menghasilkan file Excel (.xlsx) dari itinerary terstruktur.",
    instruction=INSTRUCTION,
    tools=[generate_excel_itinerary],
)
