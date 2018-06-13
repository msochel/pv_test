from sanic import Sanic
from sanic.response import json
from contact import Contact

app = Sanic()

@app.route("/backend")
async def test(request):
    data = Contact().data_contacts()
    return json({ 'data' : list(data)[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
