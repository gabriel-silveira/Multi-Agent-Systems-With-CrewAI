from crewai import Task

from agents.researcher_agent import researcher_agent

# Task for Researcher Agent: Extract Job Requirements
research_task = Task(
  description=(
    "Analyze the job posting URL provided ({job_posting_url}) "
    "to extract key skills, experiences, and qualifications "
    "required. Use the tools to gather content and identify "
    "and categorize the requirements."
  ),
  expected_output=(
    "A structured list of job requirements, including necessary "
    "skills, qualifications, and experiences."
  ),
  agent=researcher_agent,
  async_execution=True
)
