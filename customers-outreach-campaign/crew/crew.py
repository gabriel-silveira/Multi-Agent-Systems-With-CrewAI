from crewai import Crew

from agents.sales_rep_agent import sales_rep_agent
from agents.lead_sales_rep_agent import lead_sales_rep_agent
from tasks.lead_profiling_task import lead_profiling_task
from tasks.personalized_outreach_task import personalized_outreach_task

crew = Crew(
  agents=[sales_rep_agent, lead_sales_rep_agent],
  tasks=[lead_profiling_task, personalized_outreach_task],
  verbose=2,
  memory=True
)
