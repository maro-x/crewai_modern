import time
import warnings
from datetime import datetime
from crew import StoryCrew

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():

    inputs = {
        "topic": "Artificial Intelligence in Healthcare",
        "current_year": str(datetime.now().year)
    }

    retries = 3

    for i in range(retries):
        try:
            StoryCrew().crew().kickoff(inputs=inputs)
            break
        except Exception as e:
            print("Rate limit hit... waiting 25 seconds")
            time.sleep(25)

run()