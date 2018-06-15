from contact import Contact
from ticket import Ticket
from pymongo import MongoClient, errors
import os
from pprint import pprint
import itertools


class Database(object):
    """docstring for Database."""
    def __init__(self):
        self.client = MongoClient(os.getenv('DB_HOST'), 27017)
        self.db = self.client['db_freshdesk']
        self.tickets = self.db.tickets
        self.contacts = self.db.contacts
        self._ticket = Ticket()
        self._contact = Contact()


    def insert_data(self, collection='contact'):
        if not collection in ('ticket'):
            raise ValueError('The collection must be ticket')
        data = self._contact.data_contact()
        db_collection = self.contacts
        if collection == 'ticket':
            data = self._ticket.data_tickets()
            db_collection = self.tickets
        for row in data:
            try:
                db_collection.insert_one(row)
            except errors.DuplicateKeyError:
                print("User already exists")
        return True


    def check_data(self, collection):
        if not collection in ('ticket', 'contact'):
            raise ValueError('The collection must be ticket or contact')
        db_collection = self.db.tickets if collection == 'ticket' else self.db.contacts
        return list(db_collection.find())


    def update_date_big(self, collection):
        key = 'updated_at'
        try:
            return collection.find(
                {},{key: 1, '_id': 0}
            ).sort(key, -1).limit(1)[0][key]
        except IndexError as ie:
            return '1-1-1'


    def update_data(self, collection):
        updated_at_big = self.update_date_big(collection)
        update_records_found = self._ticket.data_tickets(
            f'&updated_since={updated_at_big}')

        for update in itertools.islice(update_records_found, 1, None):
            collection.update_one(
                {'_id': update['_id']},
                {'$set': update},
                upsert=True
            )

        return update_records_found


    def update_in_db(self):
        self.update_data(self.db.tickets)
        return True
