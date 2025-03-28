from crewai import Task

from agents.trading_strategy_agent import trading_strategy_agent

# Task for Trading Strategy Agent: Develop Trading Strategies
strategy_development_task = Task(
  description=(
    "Develop and refine trading strategies based on "
    "the insights from the Data Analyst and "
    "user-defined risk tolerance ({risk_tolerance}). "
    "Consider trading preferences ({trading_strategy_preference})."
  ),
  expected_output=(
    "A set of potential trading strategies for {stock_selection} "
    "that align with the user's risk tolerance."
  ),
  agent=trading_strategy_agent,
)