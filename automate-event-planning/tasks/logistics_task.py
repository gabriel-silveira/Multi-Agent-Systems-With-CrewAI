from crewai import Task

from agents.logistics_manager_agent import logistics_manager_agent

logistics_task = Task(
  description="Coordinate catering and "
              "equipment for an event "
              "with {expected_participants} participants "
              "on {tentative_date}.",
  expected_output="Confirmation of all logistics arrangements including catering and equipment setup.",
  human_input=True,
  async_execution=False,
  #async_execution=True,
  agent=logistics_manager_agent
)
