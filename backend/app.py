from sanic import Sanic
from sanic.response import json
from ticket import Ticket
from pymongo import MongoClient
from uuid import uuid4
import os
from database import Database

# data = Ticket().all_tickets()
# print(list(data))

client = MongoClient(os.getenv('DB_HOST'), 27017)
db = client['db_freshdesk']
# print(db)
# print(list(db.tickets.find()))

app = Sanic()

def get_handler(request):
    if request.method == "GET":
        return json({ 'data': list(db.tickets.find()) })
    return json({ })

app.add_route(get_handler, '/backend/get', methods=["GET"])
# app.add_route(Database().insert_ticket_db(), '/', methods=["POST"])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
