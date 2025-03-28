from crewai import Crew

from agents.interview_preparer_agent import interview_preparer_agent
from agents.profiler_agent import profiler_agent
from agents.researcher_agent import researcher_agent
from agents.resume_strategist_agent import resume_strategist_agent

from tasks.interview_preparation_task import interview_preparation_task
from tasks.profile_task import profile_task
from tasks.research_task import research_task
from tasks.resume_strategy_task import resume_strategy_task

job_application_crew = Crew(
  agents=[
    researcher_agent,
    profiler_agent,
    resume_strategist_agent,
    interview_preparer_agent,
  ],

  tasks=[
    research_task,
    profile_task,
    resume_strategy_task,
    interview_preparation_task,
  ],

  verbose=True,
)
