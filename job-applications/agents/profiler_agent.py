from crewai import Agent

from tools.tools import scrape_tool, search_tool, read_resume, semantic_search_resume

# Agent 2: Profiler
profiler_agent = Agent(
  role="Personal Profiler for Engineers",
  goal="Do incredible research on job applicants to help them stand out in the job market",
  tools=[
    scrape_tool,
    search_tool,
    read_resume,
    semantic_search_resume,
  ],
  verbose=True,
  backstory=(
    "Equipped with analytical prowess, you dissect "
    "and synthesize information "
    "from diverse sources to craft comprehensive "
    "personal and professional profiles, laying the "
    "groundwork for personalized resume enhancements."
  )
)
