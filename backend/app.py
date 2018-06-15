# Internal modules
from database import Database
from ticket import Ticket
from views import post_handler

# External libraries
from sanic import Sanic
from sanic.response import json

# Internal libraries
import os


app = Sanic()
db = Database()
tick = Ticket()

@app.middleware('response')
def cors_headers(request, response):
    cors_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Accept, Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
    }
    if response.headers is None or isinstance(response.headers, list):
        response.headers = cors_headers
    elif isinstance(response.headers, dict):
        response.headers.update(cors_headers)
    return response


def all_data_ticket(request):
    if request.method == "GET":
        return json({ 'data': db.check_data('ticket') })
    return json({ })

def all_data_contact(request):
    if request.method == "GET":
        return json({ 'data': db.check_data('contact') })
    return json({ })

def create_tickets(request, number_to_create):
      to_create = int(number_to_create)
      for _ in range(to_create):
          post_handler('tickets', vars(Ticket()))
      print('Done.')
      return json ({"Done": 1})

def insert_tickets(request):
      return json ({"Done": db.insert_data('ticket')})

def insert_contacts(request):
      return json ({"Done": db.insert_data()})

def update_contacts(request):
      return json ({"Done": db.update_in_db()})


app.add_route(create_tickets,
    '/backend/create/<number_to_create>', methods=["GET", "OPTIONS"]
    )
app.add_route(insert_tickets,
    '/backend/insert_ticket', methods=["GET", "OPTIONS"]
    )
app.add_route(insert_contacts,
    '/backend/insert_contacts', methods=["GET", "OPTIONS"]
    )
app.add_route(all_data_ticket,
    '/backend/get_ticket', methods=["GET", "OPTIONS"]
    )
app.add_route(all_data_contact,
    '/backend/get_contact', methods=["GET", "OPTIONS"]
    )
app.add_route(update_contacts,
    '/backend/update_ticker', methods=["GET", "OPTIONS"]
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
