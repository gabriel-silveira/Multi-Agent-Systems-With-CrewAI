from crewai import Crew

from agents.support import support_agent
from agents.support_qa import support_quality_assurance_agent
from tasks.inquiry_resolution import inquiry_resolution
from tasks.quality_assurance_review import quality_assurance_review

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True,
)
