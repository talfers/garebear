from log import logging
from datetime import datetime
from classes.check import Check

logger = logging.getLogger('parser.py')

class Parser:
    def __init__(self):
        pass
    

    def parse_calendar_data(self, rows):
        print(rows)
        return rows


    def convert_dates(self, date_list, format):
        new_date_list = []
        for string in date_list:
            datetime.strptime(string, format)
        return new_date_list


    def match_dates(self, found_date, start, end, blackout_dates):
        blackout_datetimes = self.convert_dates(blackout_dates, '%m/%d/%Y')
        if start <= found_date <= end:
            if found_date in blackout_datetimes:
                return Check(found_date, False, 'Found date is in blackout dates')
            else:
                return Check(found_date, True, 'Available permit found!')
        else:
            return Check(found_date, False, 'Found date not within start to end date range')
