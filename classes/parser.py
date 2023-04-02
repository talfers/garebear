from log import logging
from datetime import datetime
from bs4 import BeautifulSoup
from classes.check import Check

logger = logging.getLogger('parser.py')

class Parser:
    def __init__(self):
        pass

    def make_soup(self, page_source):
        soup = BeautifulSoup(page_source, features="html.parser")
        return soup


    def parse_calendar_data(self, rows):
        print(rows)
        sites = []
        # for site in rows:
        #     site_dates = site.find_all("div", {"class": "rec-grid-grid-cell"})
        #     site_dict = { "name": "", "dates": [] }
        #     for i in range(len(site_dates)):
        #         content = site_dates[i].find("span", {"class": "sarsa-button-content"})
        #         content = content.contents[0]
        #         button = site_dates[i].find("button")
        #         if i == 0:
        #             site_dict["name"] = content
        #             continue
        #         else:
        #             try:
        #                 label = button['aria-label']
        #                 date = label[label.find(' on ') + 4 : label.find("-") - 1]
        #                 date = datetime.strptime(date, '%B %d, %Y').strftime('%m-%d-%Y')
        #                 if int(content) > 0:
        #                     site_dict["dates"].append({"date": date, "value": int(content)})
        #             except Exception as e:
        #                 logger.error(f'Error parsing dates! Error: {e}')
        #     if site_dict['name'] != "" and len(site_dict['dates']) > 0:
        #         sites.append(site_dict)
        return sites


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
