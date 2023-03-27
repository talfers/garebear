import sys
from log import logging
from classes.config import Config
from classes.recreation import Recreation
from classes.crawler import Crawler

logger = logging.getLogger('main')
exit_code = 0

try:
        config = Config()
        rec = Recreation()
        crawler = Crawler()

        try:
            permits = rec.create_permit_objects(config.permits)
            for p in permits:
                driver = crawler.start_driver()
                driver = crawler.get_permit_url(driver, p.id, p.start_date)
                crawler.get_availiabilty_data(driver, p)
                        
        except Exception as e:
                logger.error(e)
                exit_code = 1
        
except Exception as e:
        logger.error(e)
        exit_code = 2

sys.exit(exit_code)


