from crewai import Task

from agents.marketing_communications_agent import marketing_communications_agent

marketing_task = Task(
  description="Promote the {event_topic} aiming to engage at least"
              "{expected_participants} potential attendees.",
  expected_output="Report on marketing activities and attendee engagement formatted as markdown.",
  async_execution=False,
  #async_execution=True,
  output_file="marketing_report.md",  # Outputs the report as a text file
  agent=marketing_communications_agent
)