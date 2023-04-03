from log import logging
from jinja2 import Template
from twilio.rest import Client

logger = logging.getLogger('twilio_class')

class Texter:
    def __init__(self, account_sid, auth_token, phone_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)
        self.phone_number = phone_number
    
    def sendMessage(self, to, body, media=None):
        try:
            message = self.client.messages.create(
                    body=body,
                    from_=self.phone_number,
                    media_url=media,
                    to=to
                )
            return message
        except Exception as e:
            raise Exception(e)
        

    def createMessageBody(self, p):
        rendered = ""
        with open('./email.j2') as f:
            rendered = Template(
                f.read(), 
                trim_blocks=True, 
                lstrip_blocks=True
            ).render({
                'p': p,
            })
        return rendered