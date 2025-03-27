from crewai import Task

from models.venue_details_model import VenueDetailsModel
from agents.venue_coordinator_agent import venue_coordinator_agent

venue_task = Task(
  description="Find a venue in {event_city} that meets criteria for {event_topic}.",
  expected_output="All the details of a specifically chosen venue you found to accommodate the event.",
  human_input=True,
  output_json=VenueDetailsModel,
  output_file="venue_details.json",
  # Outputs the venue details as a JSON file
  agent=venue_coordinator_agent
)
