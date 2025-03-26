from crewai import Task

from agents.planner import planner

plan = Task(
  description=(
    "1. Prioritize the latest trends, key players, "
    "and noteworthy news on {topic}.\n"
    "2. Identify the target audience, considering "
    "their interests and pain points.\n"
    "3. Develop a detailed content outline including "
    "an introduction, key points, and a call to action.\n"
    "4. Include SEO keywords and relevant data or sources."
  ),
  expected_output="A comprehensive content plan document "
                  "with an outline, audience analysis, "
                  "SEO keywords, and resources.",
  agent=planner,
)
