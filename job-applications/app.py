# Warning control
import warnings

from job_application_crew import job_application_crew

warnings.filterwarnings('ignore')

from utils.utils import get_openai_api_key, get_serper_api_key

openai_api_key = get_openai_api_key()

import os

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

job_application_inputs = {
  'job_posting_url': 'https://programathor.com.br/jobs/31757-dev-front-end-specialist',
  'github_url': 'https://github.com/gabriel-silveira',
  'personal_writeup': """Gabriel has been working in software development for over 15 years 
  with a greater focus on front-end. In recent years he has specialized in 
  building graphical tools such as vector graphics editors, flow diagrams, 
  seat maps and chatbot builders using Canvas API, SVG, Fabric.js, Joint.js among others."""
}

# this execution will take a few minutes to run
result = job_application_crew.kickoff(inputs=job_application_inputs)
