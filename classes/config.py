import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

class Config:
    def __init__(self):
        self.permits = [
            {'id': '621744', 'start_date': '2023-05-18', 'end_date': '2023-12-31', 'num_people': 2},
            {'id': '250014', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2}
        ]
        self.gov_key = os.getenv('GOV_KEY', "NOT PROVIDED")