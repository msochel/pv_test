import requests
import json
import pprint
from methods_handler import post_handler, get_handler

class Contact(object):

    def data_contacts(self):
        page = 1
        while True:
            contacts = get_handler(f'contacts?per_page=2&page={page}')
            if contacts:
                for contact in contacts:
                    yield {
                        'name': contact['name'],
                        'email': contact['email'],
                        'address': contact['address'],
                        '_id': contact['id'],
                        'created_at': contact['created_at'],
                        'updated_at': contact['updated_at']
                    }
                page += 1
            else:
                break

    def create_contact(contact):
        post_handler('contacts', contact)

# for i in Contact().data_contacts():
    # pprint.pprint(i)

# print(list(Contact().data_contacts())[0])
