from log import logging
from datetime import datetime
from bs4 import BeautifulSoup

logger = logging.getLogger('parser.py')

class Parser:
    def __init__(self):
        pass

    def make_soup(self, page_source):
        soup = BeautifulSoup(page_source, features="html.parser")
        return soup
    

    def parse_table_data(self, rows):
        sites = []
        for site in rows:
            site_dates = site.find_all("div", {"class": "rec-grid-grid-cell"})
            site_dict = { "name": "", "dates": [] }
            for i in range(len(site_dates)):
                content = site_dates[i].find("span", {"class": "sarsa-button-content"})
                content = content.contents[0]
                button = site_dates[i].find("button")
                if i == 0:
                    site_dict["name"] = content
                    continue
                else:
                    try:
                        label = button['aria-label']
                        date = label[label.find(' on ') + 4 : label.find("-") - 1]
                        date = datetime.strptime(date, '%B %d, %Y').strftime('%m-%d-%Y')
                        if int(content) > 0:
                            site_dict["dates"].append({"date": date, "value": int(content)})
                    except Exception as e:
                        logger.error(f'Error parsing dates! Error: {e}')
            if site_dict['name'] != "" and len(site_dict['dates']) > 0:
                sites.append(site_dict)
        return sites