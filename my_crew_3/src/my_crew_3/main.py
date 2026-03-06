import sys
import warnings
import time

from datetime import datetime

from crew import AnalyticalCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():

    inputs = {
        "topic": "Future of AI Agents",
        "current_year": str(datetime.now().year)
    }

   
    retries = 3

    for i in range(retries):
        try:
            AnalyticalCrew().crew().kickoff(inputs=inputs)
            break
        except Exception as e:
            print("Rate limit hit... waiting 25 seconds")
            time.sleep(25)

run()