from log import logging
from classes.permit import Permit


logger = logging.getLogger('Recreation')

class Recreation:
    def __init__(self):
        pass

    def create_permit_objects(self, permits):
        permit_objects = []
        for p in permits:
            try:
                permit_objects.append(Permit(p['id'], p['start_date'], p['end_date'], p['num_people']))
            except Exception as e:
                raise Exception(f'Error creating permit objects. Error: {e}')
        return permit_objects
        
    
    def parse_booking_data(self, data, dates):
        logger.info('parse_booking_data!')