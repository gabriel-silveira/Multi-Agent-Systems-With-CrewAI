from crewai import Agent

from tools.tools import scrape_tool, search_tool

execution_agent = Agent(
  role="Trade Advisor",
  goal="Suggest optimal trade execution strategies "
       "based on approved trading strategies.",
  backstory="This agent specializes in analyzing the timing, price, "
            "and logistical details of potential trades. By evaluating "
            "these factors, it provides well-founded suggestions for "
            "when and how trades should be executed to maximize "
            "efficiency and adherence to strategy.",
  verbose=True,
  allow_delegation=True,
  tools=[scrape_tool, search_tool]
)