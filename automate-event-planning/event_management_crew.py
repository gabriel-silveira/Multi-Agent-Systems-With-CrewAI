from crewai import Crew

from agents.logistics_manager_agent import logistics_manager_agent
from agents.marketing_communications_agent import marketing_communications_agent
from agents.venue_coordinator_agent import venue_coordinator_agent

from tasks.logistics_task import logistics_task
from tasks.marketing_task import marketing_task
from tasks.venue_task import venue_task

# Define the crew with agents and tasks
event_management_crew = Crew(
  agents=[
    venue_coordinator_agent,
    logistics_manager_agent,
    marketing_communications_agent,
  ],

  tasks=[
    venue_task,
    logistics_task,
    marketing_task,
  ],

  verbose=True
)