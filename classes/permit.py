from datetime import datetime

class Permit:
    def __init__(self, id, start_date, end_date, num_people):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.num_people = num_people
        self.start_datetime = datetime.strptime(self.start_date, '%Y-%m-%d')
        self.end_datetime = datetime.strptime(self.end_date, '%Y-%m-%d')
        self.num_days = int((self.end_datetime - self.start_datetime).days)