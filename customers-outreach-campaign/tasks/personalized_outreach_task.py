from crewai import Task

from agents.lead_sales_rep_agent import lead_sales_rep_agent
from tools.all_tools import sentiment_analysis_tool, search_tool

personalized_outreach_task = Task(
  description=(
    "Using the insights gathered from "
    "the lead profiling report on {lead_name}, "
    "craft a personalized outreach campaign "
    "aimed at {key_decision_maker}, "
    "the {position} of {lead_name}. "
    "The campaign should address their recent {milestone} "
    "and how our solutions can support their goals. "
    "Your communication must resonate "
    "with {lead_name}'s company culture and values, "
    "demonstrating a deep understanding of "
    "their business and needs.\n"
    "Don't make assumptions and only "
    "use information you absolutely sure about."
  ),
  expected_output=(
    "A series of personalized email drafts "
    "tailored to {lead_name}, "
    "specifically targeting {key_decision_maker}."
    "Each draft should include "
    "a compelling narrative that connects our solutions "
    "with their recent achievements and future goals. "
    "Ensure the tone is engaging, professional, "
    "and aligned with {lead_name}'s corporate identity."
  ),
  tools=[sentiment_analysis_tool, search_tool],
  agent=lead_sales_rep_agent,
)
