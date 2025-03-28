from crewai import Agent

from tools.tools import scrape_tool, search_tool, read_resume, semantic_search_resume

# Agent 3: Resume Strategist
resume_strategist_agent = Agent(
  role="Resume Strategist for Engineers",
  goal="Find all the best ways to make a resume stand out in the job market.",
  tools=[
    scrape_tool,
    search_tool,
    read_resume,
    semantic_search_resume,
  ],
  verbose=True,
  backstory=(
    "With a strategic mind and an eye for detail, you "
    "excel at refining resumes to highlight the most "
    "relevant skills and experiences, ensuring they "
    "resonate perfectly with the job's requirements."
  )
)
