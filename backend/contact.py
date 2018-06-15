# Internal modules
from views import post_handler, get_handler

class Contact(object):

    def data_contact(self):
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
