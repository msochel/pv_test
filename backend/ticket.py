from random import choice
import requests
import json
import pprint
from agent import Agent
from contact import Contact
from methods_handler import post_handler, get_handler

class Ticket():
    '''docstring for CreateTicket.'''
    def __init__(self):
        self.subject = self.select_value('subject')
        self.status = self.select_value('status')
        self.source = self.select_value('source')
        self.priority = self.select_value('priority')
        self.description = self.select_value('description')
        self.requester_id = self.select_value('requester_id')
        self.responder_id = self.select_value('responder_id')
        self.type = self.select_value('type')


    def select_value(self, field):
        if type(self.field_ticket[field]) is dict:
            return choice(list(self.field_ticket[field].values()))
        return choice(self.field_ticket[field])


    field_ticket = {
        'source' : {
            'Email': 1,
            'Portal': 2,
            'Phone': 3,
            'Chat': 7,
            'Mobihelp': 8,
            'Feedback Widget': 9,
            'Outbound Email': 10
        },
        'status' : {
            'Open': 2,
            'Pending': 3,
            'Resolved': 4,
            'Closed': 5
        },
        'priority' : {
            'Low': 1,
            'Medium': 2,
            'High': 3,
            'Urgent': 4
        },
        'type': ['Question', 'Incident', 'Problem'],
        'subject' : ['Help Me!', 'Please help', 'Question'],
        'description' : ['the chat channel does not work',
            'how do I make a payment', 'nobody answers me> :('],
        'responder_id' : [ ticket['_id'] for ticket in Agent.data_agent() ],
        'requester_id' : [ contact['_id'] for contact in Contact().data_contacts() ]
    }

    def find_key_by_value(self, key, value):
        keys = list(self.field_ticket[key].keys())
        value_pos = list(self.field_ticket[key].values()).index(value)
        return keys[value_pos]


        print(list(dic.keys())[list(dic.values()).index(2)])

    def all_tickets(self, query=""):
        page = 1
        while True:
            tickets = get_handler(f'tickets?per_page=5&page={page}{query}')
            if tickets:
                for ticket in tickets:
                    yield {
                        '_id': ticket['id'],
                        'updated_at': ticket['updated_at'],
                        'created_at': ticket['created_at'],
                        'status': self.find_key_by_value('status', ticket['status']),
                        'source': self.find_key_by_value('source', ticket['source']),
                        'priority': self.find_key_by_value('priority', ticket['priority']),
                        'description': ticket['description_text'],
                        'requester_id': ticket['requester_id'],
                        'name': get_handler(f"contacts/{ticket['requester_id']}")["name"],
                        'responder_id': ticket['responder_id'],
                        'type': ticket['type']
                    }
                page += 1
            else:
                break


def create_ticket(num_interactions):
    for _ in range(num_interactions):
        post_handler('tickets', Ticket().__dict__)


# if __name__ == '__main__':
#     create_ticket(2)

# create_ticket(3)
for ticker in Ticket().all_tickets():
    pprint.pprint(ticker)
# print(vars(obj))
