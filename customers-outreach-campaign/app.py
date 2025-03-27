# Warning control
import warnings

warnings.filterwarnings('ignore')

from utils.utils import (get_serper_api_key,
                         get_openai_api_key,
                         get_openai_model_name)

openai_api_key = get_openai_api_key()

import os

os.environ["OPENAI_MODEL_NAME"] = get_openai_model_name()
os.environ["SERPER_API_KEY"] = get_serper_api_key()

from crew.crew import crew

if __name__ == "__main__":
  inputs = {
    "lead_name": "DeepLearningAI",
    "industry": "Online Learning Platform",
    "key_decision_maker": "Andrew Ng",
    "position": "CEO",
    "milestone": "product launch"
  }

  result = crew.kickoff(inputs=inputs)
