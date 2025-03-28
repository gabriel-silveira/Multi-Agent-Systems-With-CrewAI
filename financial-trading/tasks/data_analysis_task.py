from crewai import Task

from agents.data_analyst_agent import data_analyst_agent

# Task for Data Analyst Agent: Analyze Market Data
data_analysis_task = Task(
  description=(
    "Continuously monitor and analyze market data for "
    "the selected stock ({stock_selection}). "
    "Use statistical modeling and machine learning to "
    "identify trends and predict market movements."
  ),
  expected_output=(
    "Insights and alerts about significant market "
    "opportunities or threats for {stock_selection}."
  ),
  agent=data_analyst_agent,
)