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

def all_data(request):
    if request.method == "GET":
        return json({ 'data': db.check_tickets_db() })
    return json({ })

def gen_tickets(request, number):
      to_create = int(number)
      for _ in range(to_create):
          post_handler('tickets', vars(Ticket()))
      print('Done.')
      return json ({"Done": 1})


def insert_tickets(request):
      return json ({"Done": db.insert_ticket_db()})


# CORS(app)
app.add_route(gen_tickets, '/backend/get/<number>', methods=["GET", "OPTIONS"])
app.add_route(insert_tickets, '/backend/insert', methods=["GET", "OPTIONS"])
app.add_route(all_data, '/backend/get', methods=["GET", "OPTIONS"])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
