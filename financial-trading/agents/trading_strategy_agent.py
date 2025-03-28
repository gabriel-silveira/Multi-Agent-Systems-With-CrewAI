from crewai import Agent

from tools.tools import scrape_tool, search_tool

trading_strategy_agent = Agent(
  role="Trading Strategy Developer",
  goal="Develop and test various trading strategies based "
       "on insights from the Data Analyst Agent.",
  backstory="Equipped with a deep understanding of financial "
            "markets and quantitative analysis, this agent "
            "devises and refines trading strategies. It evaluates "
            "the performance of different approaches to determine "
            "the most profitable and risk-averse options.",
  verbose=True,
  allow_delegation=True,
  tools=[scrape_tool, search_tool]
)