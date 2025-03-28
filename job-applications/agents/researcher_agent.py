from crewai import Agent

from tools.tools import scrape_tool, search_tool

# Agent 1: Researcher
researcher_agent = Agent(
  role="Tech Job Researcher",
  goal="Make sure to do amazing analysis on job posting to help job applicants",
  tools=[
    scrape_tool,
    search_tool,
  ],
  verbose=True,
  backstory=(
    "As a Job Researcher, your prowess in "
    "navigating and extracting critical "
    "information from job postings is unmatched."
    "Your skills help pinpoint the necessary "
    "qualifications and skills sought "
    "by employers, forming the foundation for "
    "effective application tailoring."
  )
)
