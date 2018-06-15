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

    def insert_ticket_db(self):
        data = Ticket().all_tickets()
        for ticket in data:
            try:
                self.tickets.insert_one(ticket)
            except errors.DuplicateKeyError:
                print("User already exists")
        return True

    def insert_contact_db(self):
        data = Contact().data_contact()
        for contact in data:
            try:
                self.contacts.insert_one(contact)
            except errors.DuplicateKeyError:
                print("User already exists")
        return True


    def check_tickets_db(self):
        return list(self.db.tickets.find())


    def check_contacts_db(self):
        return list(self.db.contacts.find())


    def __greater_local_date(self, collection, date_type):
        if not date_type in ('created', 'updated'):
            raise ValueError('The date type must be \'created\' or \'updated\'')

        date_field: str = 'created_at' if date_type == 'created' else 'updated_at'
        try:
            return collection.find(
                {},{date_field: 1, '_id': 0}
            ).sort(date_field, -1).limit(1)[0][date_field]
        except IndexError as ie:
            return '1-1-1'

    def update_data(self, collection, save=False):
        # Selects que class for queries
        Queries = Ticket()

        updated_gld = self.__greater_local_date(collection, 'updated')
        update_records_found = Ticket().all_tickets(
            f'&updated_since={updated_gld}')

        for update in itertools.islice(update_records_found, 1, None):
            collection.update_one({'_id': update['_id']}, {'$set': update})

        return update_records_found


# obj = Database()
    def test(self):
        self.insert_ticket_db()
        # print(self.__greater_local_date(self.db.tickets, 'updated'))
        # for x in itertools.islice(self.update_data(self.db.tickets), 1, None):
        #    pprint(x)
        # print(self.__greater_local_date(self.db.tickets, 'created'))
        self.update_data(self.db.tickets)
    # print(obj.database, )
# insert_user_db(obj.check_tickets_db())

if __name__ == '__main__':
    obj = Database()
    # obj.insert_ticket_db()
    # obj.test()
# pprint(list(db.tickets.find()))
