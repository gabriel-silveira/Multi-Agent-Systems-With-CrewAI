from crewai import Task

from agents.support_qa import support_quality_assurance_agent

quality_assurance_review = Task(
  description=(
    "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
    "Ensure that the answer is comprehensive, accurate, and adheres to the "
    "high-quality standards expected for customer support.\n"
    "Verify that all parts of the customer's inquiry "
    "have been addressed "
    "thoroughly, with a helpful and friendly tone.\n"
    "Check for references and sources used to "
    " find the information, "
    "ensuring the response is well-supported and "
    "leaves no questions unanswered."
  ),
  expected_output=(
    "A final, detailed, and informative response "
    "ready to be sent to the customer.\n"
    "This response should fully address the "
    "customer's inquiry, incorporating all "
    "relevant feedback and improvements.\n"
    "Don't be too formal, we are a chill and cool company "
    "but maintain a professional and friendly tone throughout."
  ),
  agent=support_quality_assurance_agent,
)
