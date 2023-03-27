import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from classes.parser import Parser

parser = Parser()

class Crawler:
    def __init__(self):
        self.url = "https://www.recreation.gov/permits"
        self.driver = None
        self.numPeopleButtonId = "guest-counter-QuotaUsageByMember"
        self.numPeopleInputId = "guest-counter-QuotaUsageByMember-number-field-People"
        self.districtPickerClass = "district-picker-section"

    def start_driver(self):
        driver = webdriver.Firefox()
        return driver
    
    def get_url(self, driver, site_id, date):
        driver.implicitly_wait(30)
        driver.get(f'{self.url}/{site_id}/registration/detailed-availability?date={date}')
        driver.implicitly_wait(30)
        return driver

    def input_num_people(self, driver, num_people):
        people_button = driver.find_element("id", self.numPeopleButtonId)
        people_button.click()
        people_input = driver.find_element("id", self.numPeopleInputId)
        people_input.send_keys(str(num_people))
        people_button.click()
        return driver

    def get_availiabilty_data(self, driver, num_people):
        try:
            self.input_num_people(driver, num_people)
            soup = parser.makeSoup(driver.page_source)
            rows = soup.find_all("div", {"class": "rec-grid-row"})
            print(rows)
            # sites_dict = parser.parseTableData(rows)
            # with open("all_permits.json", "w") as outfile:
            #     json.dump(sites_dict, outfile, indent=4, sort_keys=True)
            
        except Exception as e:
            print("Couldnt find num people input!!", e)
            try:
                district_picker = driver.find_element(By.CLASS_NAME, self.districtPickerClass)
                btns = district_picker.find_elements(By.TAG_NAME, 'button')
                for btn in btns:
                    print(btn)
                    # btn.click()
                    # soup = parser.makeSoup(driver.page_source)
                    # rows = soup.find_all("div", {"class": "rec-grid-row"})
                    # sites_dict = parser.parseTableData(rows)
                    # with open("all_campsites.json", "w") as outfile:
                    #     json.dump(sites_dict, outfile, indent=4, sort_keys=True)
            except Exception as e:
                print("Couldnt find district picker!!", e)
                soup = parser.makeSoup(driver.page_source)
                rows = soup.find_all("div", {"class": "rec-grid-row"})
                sites_dict = parser.parseTableData(rows)
                with open("all_campsites.json", "w") as outfile:
                    json.dump(sites_dict, outfile, indent=4, sort_keys=True)

    
    
    ##############################
    ##############################
    
    

    def check_rec_bookings(self, p):
        print(p.end_datetime)
        # crawler.getUrl(f['id'], f[start_date])
        # crawler.loop_districts(f['num_people'])
        ######
        # crawler.inputData(num_people)
        # soup = crawler.makeSoup()
        # rows = soup.find_all("div", {"class": "rec-grid-row"})
        # sites_dict = crawler.parseTableData(rows)
        # with open("all_campsites.json", "w") as outfile:
        #     json.dump(sites_dict, outfile, indent=4, sort_keys=True)
        # check_history = self.parse_booking_data(sites_dict)
        # break
        # return check_history

    
    