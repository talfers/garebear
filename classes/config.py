import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

class Config:
    def __init__(self):
        self.permits = [
            {'id': '250014', 'start_date': '2023-05-18', 'end_date': '2023-12-31', 'num_people': 2, 'section': 'Gates of Lodore, Green River'},
            {'id': '250014', 'start_date': '2023-05-18', 'end_date': '2023-12-31', 'num_people': 2, 'section': 'Deerlodge Park, Yampa River'},
            {'id': '233393', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2, 'section': ''},
            {'id': '250986', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2, 'section': 'Mexican Hat to Clay Hills'},
            {'id': '234623', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2, 'section': ''},
            {'id': '234622', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2, 'section': ''},
            {'id': '621743', 'start_date': '2023-12-11', 'end_date': '2023-12-31', 'num_people': 2, 'section': ''}
        ]
        self.gov_key = os.getenv('GOV_KEY', "NOT PROVIDED")
