from crewai import Task

from agents.execution_agent import execution_agent

# Task for Trade Advisor Agent: Plan Trade Execution
execution_planning_task = Task(
  description=(
    "Analyze approved trading strategies to determine the "
    "best execution methods for {stock_selection}, "
    "considering current market conditions and optimal pricing."
  ),
  expected_output=(
    "Detailed execution plans suggesting how and when to "
    "execute trades for {stock_selection}."
  ),
  agent=execution_agent,
)