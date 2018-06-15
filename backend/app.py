from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
import os
from database import Database
from ticket import Ticket
from methods_handler import post_handler


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
        return json({ 'data': db.check_tickets_db() })
    return json({ })

def all_data_contact(request):
    if request.method == "GET":
        return json({ 'data': db.check_contacts_db() })
    return json({ })

def create_tickets(request, number_to_create):
      to_create = int(number_to_create)
      for _ in range(to_create):
          post_handler('tickets', vars(Ticket()))
      print('Done.')
      return json ({"Done": 1})

def insert_tickets(request):
      return json ({"Done": db.insert_ticket_db()})

def insert_contacts(request):
      return json ({"Done": db.insert_contact_db()})



# CORS(app)
app.add_route(create_tickets,
    '/backend/get/<number_to_create>', methods=["GET", "OPTIONS"]
    )
app.add_route(insert_tickets,
    '/backend/insert', methods=["GET", "OPTIONS"]
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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
