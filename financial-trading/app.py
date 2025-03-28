# Warning control
import warnings

from financial_trading_crew import financial_trading_crew

warnings.filterwarnings('ignore')

from utils.utils import get_openai_api_key, get_serper_api_key

openai_api_key = get_openai_api_key()

import os

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Example data for kicking off the process
inputs = {
    'stock_selection': 'TSLA',
    'initial_capital': '100000',
    'risk_tolerance': 'Medium',
    'trading_strategy_preference': 'Swing Trading',
    'news_impact_consideration': True
}

### this execution will take some time to run
result = financial_trading_crew.kickoff(inputs=inputs)