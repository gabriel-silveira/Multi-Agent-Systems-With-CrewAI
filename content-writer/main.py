import warnings
import os

from utils.utils import get_openai_api_key

warnings.filterwarnings('ignore')

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

topic = input("What content would you like me to create?\n")

from crew import crew

result = crew.kickoff(inputs={"topic": topic})
