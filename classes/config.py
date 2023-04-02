import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

class Config:
    def __init__(self):
        self.gov_key = os.getenv('GOV_KEY', "NOT PROVIDED")
