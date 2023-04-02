import sys
from log import logging
from classes.config import Config
from classes.recreation import Recreation
from classes.crawler import Crawler
from classes.sheets import Sheets
from classes.parser import Parser

logger = logging.getLogger('main')
exit_code = 0

try:
        config = Config()
        rec = Recreation()
        crawler = Crawler()
        sheets = Sheets('rec_gov_permits')
        parser = Parser()

        try:
            permits_df = sheets.get_tab_as_df('permits')
            blackout_dates = sheets.get_tab_as_df('blackout_dates')['dates'].tolist()
            permits = rec.create_permit_objects(permits_df)
            for p in permits:
                driver = crawler.start_driver()
                driver = crawler.get_permit_url(driver, p.id, p.start_date)
                data = crawler.get_availiabilty_data(driver, p)
                driver.quit()

        except Exception as e:
                logger.error(e)
                exit_code = 1

except Exception as e:
        logger.error(e)
        exit_code = 2

sys.exit(exit_code)
