import pandas as pd


class Parser():
    def __init__(self):
        pass
        
    def pullAvail(self , driver , p):
        df = pd.DataFrame( columns=['date'])
        availible_days_td = driver.find_elements(By.CSS_SELECTOR, "td[class*='CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2']")
        for i in availible_days_td:
            g = i.get_attribute('aria-label')
            df.loc[len(df.index)] = [g] 
            avail_dates_json = df.to_json(orient = "table")
            avail_rates_json = avail_rates_json[avail_rates_json.find("data")+6:len(avail_rates_json)-1]
            obj = {'id': p.id, 'section': p.section, 'dates': avail_rates_json}

        return obj

   