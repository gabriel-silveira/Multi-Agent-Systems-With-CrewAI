from agents.editor import editor
from agents.planner import planner
from agents.writer import writer
from tasks.edit import edit
from tasks.plan import plan
from tasks.write import write
from crewai import Crew

crew = Crew(
  agents=[planner, writer, editor],
  tasks=[plan, write, edit],
  verbose=2,
)
