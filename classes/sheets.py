from log import logging
import pygsheets

logger = logging.getLogger('sheets.py')

class Sheets():
    def __init__(self, sheet_name):
        self.gc = pygsheets.authorize(service_file='gcp_creds.json')
        self.sheet = self.gc.open(sheet_name)


    def get_tab_as_df(self, sheet_tab_name):
        try:
            wks = self.sheet.worksheet('title', sheet_tab_name)
            df = wks.get_as_df()
            return df
        except Exception as e:
            raise Exception(f'Error getting google sheet! Error: {e}')