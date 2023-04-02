from log import logging
from classes.permit import Permit


logger = logging.getLogger('recreation.py')

class Recreation:
    def __init__(self):
        self.num_people = 2
        


    def create_permit_objects(self, permits_df):
        permit_objects = []
        for row in permits_df.itertuples():
            url = getattr(row, 'url')
            id = url[url.find('permits/')+8:]
            try:
                permit_objects.append(Permit(id, getattr(row, 'name'), getattr(row, 'start'), getattr(row, 'end'), self.num_people, getattr(row, 'section')))
            except Exception as e:
                logger.error(e)
        return permit_objects


    def parse_booking_data(self, data, dates):
        logger.info('parse_booking_data!')
