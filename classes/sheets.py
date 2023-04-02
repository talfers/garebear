from log import logging
import pygsheets

logger = logging.getLogger('sheets.py')

class Sheets():
    def __init__(self, sheet_name):
        self.gc = pygsheets.authorize(service_file='garebear-382519-ca75277f19dc.json')
        self.sheet = self.gc.open(sheet_name)
        logger.info("sheets was initialized")


    def get_tab_as_df(self, sheet_tab_name):
        try:
            self.wks = self.sheet.worksheet('title', sheet_tab_name)
            df = self.wks.get_as_df()
            return df
        except Exception as e:
            raise Exception(f'Error getting google sheet! Error: {e}')