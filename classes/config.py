import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

class Config:
    def __init__(self):
        self.twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID', "NOT PROVIDED")
        self.twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN', "NOT PROVIDED")
        self.twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER', "NOT PROVIDED")

    def __str__(self):
        return f"twilio_phone_number: {self.twilio_phone_number}"
