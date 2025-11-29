# agents/travel_root_agent.py
import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner

# load .env
load_dotenv()

# import sub-agents (they register their tools)
from agents.sub_agents.maps_agent import maps_agent
from agents.sub_agents.booking_agent import booking_agent
from agents.sub_agents.format_agent import format_agent
from agents.sub_agents.excel_agent import excel_agent

INSTRUCTION = (
    "You are NaviTrip, a friendly travel planner orchestrator. "
    "You receive user requirements (destination, days, budget, preferences). "
    "Decompose the task to specialized sub-agents (maps_agent, booking_agent, format_agent, excel_agent). "
    "Coordinate: request location/routing from maps_agent, hotel & transport from booking_agent, "
    "format output via format_agent, and produce spreadsheet via excel_agent when requested. "
    "Speak in Indonesian."
)

root_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="travel_itinerary_root",
    description="Root orchestrator that coordinates maps, booking, formatting, and excel export agents.",
    instruction=INSTRUCTION,
    # register sub-agents so ADK can route tasks to them
    agents=[maps_agent, booking_agent, format_agent, excel_agent],
)

# Optional quick runner for CLI testing (non-ADK UI)
if __name__ == "__main__":
    runner = InMemoryRunner(root_agent)
    prompt = "Buatkan itinerary 2 hari di Puncak untuk 2 orang, gaya santai, budget medium. Sertakan file Excel."
    print("Running sample prompt (non-ADK). This is just for quick local test.")
    resp = runner.run(prompt)
    print(resp)
