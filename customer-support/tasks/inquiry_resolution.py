from crewai import Task

from agents.support import support_agent
from tools.docs_scrape import docs_scrape_tool

inquiry_resolution = Task(
  description=(
    "{customer} just reached out with a super important ask:\n"
    "{inquiry}\n\n"
    "{person} from {customer} is the one that reached out. "
    "Make sure to use everything you know "
    "to provide the best support possible."
    "You must strive to provide a complete "
    "and accurate response to the customer's inquiry."
  ),
  expected_output=(
    "A detailed, informative response to the "
    "customer's inquiry that addresses "
    "all aspects of their question.\n"
    "The response should include references "
    "to everything you used to find the answer, "
    "including external data or solutions. "
    "Ensure the answer is complete, "
    "leaving no questions unanswered, and maintain a helpful and friendly "
    "tone throughout."
  ),
  tools=[docs_scrape_tool],
  agent=support_agent,
)
