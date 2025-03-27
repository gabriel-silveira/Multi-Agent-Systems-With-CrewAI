from crewai import Agent

from tools.all_tools import search_tool, scrape_tool

# Agent 1: Venue Coordinator
venue_coordinator_agent = Agent(
  role="Venue Coordinator",
  goal="Identify and book an appropriate venue based on event requirements",
  tools=[search_tool, scrape_tool],
  verbose=True,
  backstory=(
    "With a keen sense of space and "
    "understanding of event logistics, "
    "you excel at finding and securing "
    "the perfect venue that fits the event's theme, "
    "size, and budget constraints."
  )
)
