from log import logging
import json, time
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
        self.num_people_button_id_2 = "guest-counter"
        self.num_people_input_id = "guest-counter-QuotaUsageByMember-number-field-People"
        self.num_people_input_id_2 = "guest-counter-number-field-People"
        self.district_picker_class = "district-picker-section"
        self.date_picker_id = "jump-date"


    def start_driver(self):
        driver = webdriver.Firefox()
        return driver
    

    def get_permit_url(self, driver, permit_id, date):
        driver.get(f'{self.url}/{permit_id}/registration/detailed-availability?date={date}')
        return driver
    

    def get_district_buttons(self, driver):
        btns = []
        district_picker = driver.find_elements(By.XPATH, f"//div[@class='{self.district_picker_class}']")
        if len(district_picker) > 0:
            btns = district_picker[0].find_elements(By.TAG_NAME, 'button')
        return btns


    def input_num_people(self, driver, num_people):
        num_people_buttons = driver.find_elements(By.XPATH, f"//button[@id='{self.num_people_button_id}' or @id='{self.num_people_button_id_2}']")
        if len(num_people_buttons) > 0:
            num_people_buttons[0].click()
        num_people_inputs = driver.find_elements(By.XPATH, f"//input[@id='{self.num_people_input_id}' or @id='{self.num_people_input_id_2}']")
        if len(num_people_inputs) > 0:
            num_people_inputs[0].send_keys(str(num_people))
            num_people_buttons[0].click()
        return driver
    

    def input_date(self, driver, date):   
        date_converted = date.strftime("%m/%d/%Y")
        date_inputs = driver.find_elements(By.XPATH, f"//input[@id='{self.date_picker_id}']")
        if len(date_inputs) > 0:
            date_inputs[0].send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
            date_inputs[0].send_keys(str(date_converted[1:]))
            v = date_inputs[0].get_attribute("value")
            if v != date_converted[0]:
                date_inputs[0].send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT ,Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.ARROW_LEFT, Keys.BACKSPACE, date_converted[:1] )
            date_inputs[0].send_keys(Keys.TAB)
            time.sleep(1.25)
        return driver


    def get_availiabilty_data(self, driver, p):

        try:
            self.input_num_people(driver, p.num_people)
            self.input_date(driver, p.start_datetime)
            district_btns = self.get_district_buttons(driver)
            if len(district_btns) > 0:
                all_districts_list = []
                for btn in district_btns:
                    district = btn.get_attribute("name")
                    district_dict = { 'name': district, 'sites': [] }
                    btn.click()
                    soup = parser.make_soup(driver.page_source)
                    rows = soup.find_all("div", {"class": "rec-grid-row"})
                    # sites_dict = parser.parse_table_data(rows)
                    # district_dict['sites'].extend(sites_dict)
                #     all_districts_list.append(district_dict)
                # with open(f"./data/{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
                #     json.dump(all_districts_list, outfile, indent=4, sort_keys=True)

            else:
                soup = parser.make_soup(driver.page_source)
                rows = soup.find_all("div", {"class": "rec-grid-row"})
                sites_dict = parser.parse_table_data(rows)
                with open(f"./data/{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
                    json.dump(sites_dict, outfile, indent=4, sort_keys=True)
                return sites_dict
            
        except Exception as e:
            logger.error(f"Error parsing table!! Error: {e}")
            