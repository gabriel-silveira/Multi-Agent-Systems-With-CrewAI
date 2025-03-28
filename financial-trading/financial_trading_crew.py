from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from agents.data_analyst_agent import data_analyst_agent
from agents.execution_agent import execution_agent
from agents.risk_management_agent import risk_management_agent
from agents.trading_strategy_agent import trading_strategy_agent
from tasks.data_analysis_task import data_analysis_task
from tasks.execution_planning_task import execution_planning_task
from tasks.risk_assessment_task import risk_assessment_task
from tasks.strategy_development_task import strategy_development_task

# Define the crew with agents and tasks
financial_trading_crew = Crew(
  agents=[
    data_analyst_agent,
    trading_strategy_agent,
    execution_agent,
    risk_management_agent,
  ],

  tasks=[
    data_analysis_task,
    strategy_development_task,
    execution_planning_task,
    risk_assessment_task,
  ],

  manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
  process=Process.hierarchical,
  verbose=True
)
