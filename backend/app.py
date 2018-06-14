from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
import os
from database import Database


app = Sanic()

def get_handler(request):
    if request.method == "GET":
        return json({ 'data': Database().check_tickets_db() })
    return json({ })


CORS(app)
app.add_route(get_handler, '/backend/get', methods=["GET", "OPTIONS"])
app.add_route(Database().insert_ticket_db(), '/', methods=["POST", "OPTIONS"])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
