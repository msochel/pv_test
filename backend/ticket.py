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
            'Mobilhelp': 8,
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
        'subject' : ['Help Me!', 'Please help', 'Question'],
        'description' : ['the chat channel does not work',
            'how do I make a payment', 'nobody answers me> :('],
        'responder_id' : [ ticket['_id'] for ticket in Agent.all_agent() ],
        'requester_id' : [ contact['_id'] for contact in Contact().data_contacts() ]
    }

    def all_tickets(self):
        page = 1
        while True:
            tickets = get_handler(f'tickets?per_page=2&page={page}')
            if tickets:
                for ticket in tickets:
                    yield {
                        'updated_at': ticket['updated_at'],
                        'status': ticket['status'],
                        'source': ticket['source'],
                        'priority': ticket['priority'],
                        'description': ticket['description_text'],
                        'requester_id': ticket['requester_id'],
                        'responder_id': ticket['responder_id']
                    }
                page += 1
            else:
                break


def create_ticket(num_interactions):
    for _ in range(num_interactions):
        post_handler('tickets', Ticket().__dict__)


if __name__ == '__main__':
    create_ticket(3)

# create_ticket(3)

# for ticker in Ticket().all_tickets():
#    pprint.pprint(ticker)
# print(vars(obj))
