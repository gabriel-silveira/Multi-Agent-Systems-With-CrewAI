from crewai import Task

from agents.profiler_agent import profiler_agent

# Task for Profiler Agent: Compile Comprehensive Profile
profile_task = Task(
  description=(
    "Compile a detailed personal and professional profile "
    "using the GitHub ({github_url}) URLs, and personal write-up "
    "({personal_writeup}). Utilize tools to extract and "
    "synthesize information from these sources."
  ),
  expected_output=(
    "A comprehensive profile document that includes skills, "
    "project experiences, contributions, interests, and "
    "communication style."
  ),
  agent=profiler_agent,
  async_execution=True
)
