import warnings
import os

from crew import crew
from utils.utils import get_openai_api_key

warnings.filterwarnings('ignore')

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

if __name__ == "__main__":
  person_name = input("Hello, what's your name?\n")
  customer_name = input("And what's the name of your company?\n")
  inquiry_text = input(f"How can i help you, {person_name}?\n")

  inputs = {
    "customer": customer_name,
    "person": person_name,
    "inquiry": inquiry_text
  }

  result = crew.kickoff(inputs=inputs)
