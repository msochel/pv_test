from contact import Contact
from ticket import Ticket
from pymongo import MongoClient, errors
import os


client = MongoClient(os.getenv('DB_HOST'), 27017)
db = client['test-database']

data = Contact().data_contacts()
data_tickets = Ticket().all_tickets()

def insert_user_db(data):
    for user in data:
        try:
            insert = db.tickets.insert_one(user)
        except errors.DuplicateKeyError:
            print("User already exists")

insert_user_db(data_tickets)
