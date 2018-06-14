from contact import Contact
from ticket import Ticket
from pymongo import MongoClient, errors
import os
from pprint import pprint


class Database(object):
    """docstring for Database."""
    def __init__(self):
        self.client = MongoClient(os.getenv('DB_HOST'), 27017)
        self.db = self.client['db_freshdesk']
        self.tickets = self.db.tickets

    # data = Contact().data_contacts()

    def insert_ticket_db(self):
        data = Ticket().all_tickets()
        for ticket in data:
            try:
                insert = self.tickets.insert_one(ticket)
            except errors.DuplicateKeyError:
                print("User already exists")



# insert_user_db(data_tickets)


# pprint(list(db.tickets.find()))
