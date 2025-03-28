from crewai import Task

from agents.risk_management_agent import risk_management_agent

# Task for Risk Advisor Agent: Assess Trading Risks
risk_assessment_task = Task(
  description=(
    "Evaluate the risks associated with the proposed trading "
    "strategies and execution plans for {stock_selection}. "
    "Provide a detailed analysis of potential risks "
    "and suggest mitigation strategies."
  ),
  expected_output=(
    "A comprehensive risk analysis report detailing potential "
    "risks and mitigation recommendations for {stock_selection}."
  ),
  agent=risk_management_agent,
)