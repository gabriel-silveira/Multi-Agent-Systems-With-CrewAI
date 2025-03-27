# Warning control
import warnings

warnings.filterwarnings('ignore')

from utils.utils import get_openai_api_key, get_serper_api_key

openai_api_key = get_openai_api_key()

import os

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

from event_management_crew import event_management_crew

event_details = {
  'event_topic': "Tech Innovation Conference",
  'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
  'event_city': "San Francisco",
  'tentative_date': "2024-09-15",
  'expected_participants': 500,
  'budget': 20000,
  'venue_type': "Conference Hall"
}

result = event_management_crew.kickoff(inputs=event_details)

import json
from pprint import pprint

with open('venue_details.json') as f:
   data = json.load(f)

pprint(data)