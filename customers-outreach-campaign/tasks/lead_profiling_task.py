from crewai import Task

from agents.sales_rep_agent import sales_rep_agent
from tools.all_tools import directory_read_tool, file_read_tool, search_tool

lead_profiling_task = Task(
  description=(
    "Conduct an in-depth analysis of {lead_name}, "
    "a company in the {industry} sector "
    "that recently showed interest in our solutions. "
    "Utilize all available data sources "
    "to compile a detailed profile, "
    "focusing on key decision-makers, recent business "
    "developments, and potential needs "
    "that align with our offerings. "
    "This task is crucial for tailoring "
    "our engagement strategy effectively.\n"
    "Don't make assumptions and "
    "only use information you absolutely sure about."
  ),
  expected_output=(
    "A comprehensive report on {lead_name}, "
    "including company background, "
    "key personnel, recent milestones, and identified needs. "
    "Highlight potential areas where "
    "our solutions can provide value, "
    "and suggest personalized engagement strategies."
  ),
  tools=[directory_read_tool, file_read_tool, search_tool],
  agent=sales_rep_agent,
)
