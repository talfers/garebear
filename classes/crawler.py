from log import logging
import json, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from classes.parser import Parser
from selenium.webdriver.support.ui import Select

logger = logging.getLogger('crawler.py')

parser = Parser()

class Crawler:
    def __init__(self):
        self.url = "https://www.recreation.gov/permits"
        self.division_selector = "division-selection"
        self.people_input = "number-input-"
        self.next_availiable_button = '//*[@id="page-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button[3]'


    def start_driver(self):
        driver = webdriver.Firefox()
        return driver


    def get_permit_url(self, driver, permit_id, date):
        driver.get(f'{self.url}/{permit_id}')
        return driver


    def get_division_selection(self, driver, division):
        division_selector = driver.find_elements(By.XPATH, f"//select[@id='{self.division_selector}']")
        if len(division_selector) > 0:
            print(division_selector[0])
            select = Select(division_selector[0])
            select.select_by_visible_text(division);
        return driver


    def get_people_input(self, driver):
        people_input = driver.find_elements(By.XPATH, f"//input[@id='{self.people_input}']")
        if len(people_input) > 0:
            num_people_inputs[0].send_keys(str(2))
        return driver


    def get_next_availiable(self, driver):
        next_avail_button = driver.find_elements(By.XPATH, self.next_availiable_button)
        if len(next_avail_button) > 0:
            next_avail_button[0].click()
        return driver


    def get_availiabilty_data(self, driver, p):
        try:
            self.get_division_selection(driver, p.section)
            self.get_people_input(driver)
            self.get_next_availiable(driver)
            # soup = parser.make_soup(driver.page_source)
            # rows = soup.find_all("div", {"class": "rec-grid-row"})
            # sites_dict = parser.parse_table_data(rows)
            # with open(f"./data/{p.id}.{p.start_date}.{p.end_date}.json", "w") as outfile:
            #     json.dump(sites_dict, outfile, indent=4, sort_keys=True)
            # return sites_dict

        except Exception as e:
            logger.error(f"Error parsing table!! Error: {e}")
