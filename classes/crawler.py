from log import logging
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from classes.parser import Parser

logger = logging.getLogger('crawler.py')

parser = Parser()

class Crawler:
    def __init__(self):
        self.url = "https://www.recreation.gov/permits"
        self.num_people_button_id = "guest-counter-QuotaUsageByMember"
        self.num_people_input_id = "guest-counter-QuotaUsageByMember-number-field-People"
        self.district_picker_class = "district-picker-section"
        self.date_picker_id = "jump-date"


    def start_driver(self):
        driver = webdriver.Firefox()
        return driver
    

    def get_permit_url(self, driver, permit_id, date):
        driver.get(f'{self.url}/{permit_id}/registration/detailed-availability?date={date}')
        return driver


    def input_num_people(self, driver, num_people):
        people_button = driver.find_element("id", self.num_people_button_id)
        people_button.click()
        people_input = driver.find_element("id", self.num_people_input_id)
        people_input.send_keys(str(num_people))
        people_button.click()
        return driver
    

    def input_date(self, driver, date):
        date_converted = date.strftime("%m/%d/%Y")
        date_input = driver.find_element("id", self.date_picker_id)
        date_input.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
        date_input.send_keys(str(date_converted[1:]))
        v = date_input.get_attribute("value")
        if v != date_converted[0]:
            date_input.send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT ,Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.BACKSPACE, date_converted[:1] )
        driver.implicitly_wait(200)
        return driver


    def get_availiabilty_data(self, driver, p):

        ## CONDITION 1 - GUEST NUMBER AND DATE INPUT THEN DOWNLOAD TABLE DATA ##
        try:
            self.input_num_people(driver, p.num_people)
            self.input_date(driver, p.start_datetime)
            soup = parser.make_soup(driver.page_source)
            rows = soup.find_all("div", {"class": "rec-grid-row"})
            sites_dict = parser.parse_table_data(rows)
            with open(f"{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
                json.dump(sites_dict, outfile, indent=4, sort_keys=True)
            return sites_dict
            
        except Exception as e:

            ## CONDITION 2 - DISTRICT PICKER BUTTONS THEN DOWNLOAD TABLE DATA FOR EACH DISTRICT ##
            logger.warning(f"Couldnt find num people input!! Error: {e}")
            try:
                district_picker = driver.find_element(By.CLASS_NAME, self.district_picker_class)
                btns = district_picker.find_elements(By.TAG_NAME, 'button')
                for btn in btns:
                    btn.click()
                    soup = parser.make_soup(driver.page_source)
                    rows = soup.find_all("div", {"class": "rec-grid-row"})
                    print("DISTRICT PICKER")
                    # print(rows)
                    # sites_dict = parser.parse_table_data(rows)
                    # print(sites_dict)
                    # with open(f"{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
                    #     json.dump(sites_dict, outfile, indent=4, sort_keys=True)
                    # return sites_dict

            except Exception as e:
                
                ## CONDITION 3 - NO ADDITIONAL INPUT NEEDED JUST DOWNLOAD THE TABLE ##
                logger.warning(f"Couldnt find district picker!! Error: {e}")
                soup = parser.make_soup(driver.page_source)
                rows = soup.find_all("div", {"class": "rec-grid-row"})
                sites_dict = parser.parse_table_data(rows)
                with open(f"{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
                    json.dump(sites_dict, outfile, indent=4, sort_keys=True)
                return sites_dict