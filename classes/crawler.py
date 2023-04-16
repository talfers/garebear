from log import logging
import json
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from classes.parser import Parser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('crawler.py')

parser = Parser()

class Crawler:
    def __init__(self):
        self.url = "https://www.recreation.gov/permits"
        self.division_selector = "division-selection"
        self.people_input = "number-input-"
        self.next_availiable_button = '//*[@id="page-content"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button[3]'
        self.current_month_tag = "//div[@class='CalendarMonthGrid_month__horizontal CalendarMonthGrid_month__horizontal_1']//div[@class='CalendarMonth CalendarMonth_1']//div[@class='CalendarMonth_caption CalendarMonth_caption_1']//strong[1]"
        self.next_month_button = "//div[@class='sarsa-day-picker-range-controller-month-navigation-button right']"
    def start_driver(self):
        driver = webdriver.Firefox()
        return driver


    def get_permit_url(self, driver, permit_id, date):
        driver.get(f'{self.url}/{permit_id}')
        return driver


    def select_division(self, driver, division):
        division_selector = driver.find_elements(By.XPATH, f"//select[@id='{self.division_selector}']")
        if len(division_selector) > 0:
            select = Select(division_selector[0])
            select.select_by_visible_text(division);
        return driver


    def input_num_people(self, driver):
        people_input = driver.find_elements(By.XPATH, f"//input[@id='{self.people_input}']")
        if len(people_input) > 0:
            people_input[0].send_keys(str(2))
        return driver


    def click_next_availiable(self, driver):
        try:
            next_avail_button = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.next_availiable_button))
            )
        finally:
            if len(next_avail_button) > 0:
                next_avail_button[0].click()
            return driver
    

    def get_next_month_button(self, driver):
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.next_month_button))
            )
        finally:
            if len(next_button) > 0:
                return next_button[0]
            else:
                return None


    def get_current_month(self, driver):
        # month_name_tag = driver.find_elements(By.XPATH, self.current_month_tag)
        try:
            month_name_tag = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.current_month_tag))
            )
        finally:
            if len(month_name_tag) > 0:
                current_month_datetime = datetime.strptime(month_name_tag[0].text, '%B %Y')
                return current_month_datetime
            else:
                return None

    def parse_calendar_data(self, driver, p):
        df = pd.DataFrame( columns=['date'])
        dates = []
        availible_days_td = driver.find_elements(By.CSS_SELECTOR, "td[class*='CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2']")
        if len(availible_days_td) > 0:
            for i in availible_days_td:
                g = i.get_attribute('aria-label')
                df.loc[len(df.index)] = [g] 
                dates_temp = df['date'].tolist()
                dates.extend(dates_temp)
        return dates


    def get_availiable_dates(self, driver, p):
        dates = []
        try:
            self.select_division(driver, p.section)
            self.input_num_people(driver)
            self.click_next_availiable(driver)
            current_month_datetime = self.get_current_month(driver)
            next_month_button = self.get_next_month_button(driver)
            print("START CURRENT MONTH", current_month_datetime)
            print("PERMIT START", p.start_datetime, "PERMIT END", p.end_datetime)
            if current_month_datetime > p.end_datetime:
                return dates
            if current_month_datetime < p.start_datetime:
                while current_month_datetime < p.start_datetime:
                    next_month_button.click()
                    current_month_datetime = self.get_current_month(driver)
            while current_month_datetime >= p.start_datetime and current_month_datetime <= p.end_datetime:
                try:
                    next_month_button.click()
                    current_month_datetime = self.get_current_month(driver)
                    partial_dates = self.parse_calendar_data(driver, p)
                    dates.extend(partial_dates)
                    print("CURRENT MONTH", current_month_datetime)
                except Exception as e:
                    logger.error(f"Error looping through months! Error: {e}")
            print("DONE!")
            print(dates)
            return dates
        except Exception as e:
            logger.error(f"Error parsing table!! Error: {e}")
