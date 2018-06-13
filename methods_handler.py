import requests
import json

api_url = 'https://msochel.freshdesk.com/api/v2'
api_key = 'gAMalklkrYAQPTvsscu'
password = 'Mauro2209'

headers = {'Content-Type': 'application/json'}

def get_handler(endpoint):
    req = requests.get(
        f'{api_url}/{endpoint}',
        auth=(api_key, password),
        headers=headers)
    response = json.loads(req.content)
    if req.status_code == 200:
        return response
    return req.status_code


def post_handler(endpoint, data):
    req = requests.post(
        f'{api_url}/{endpoint}',
        auth=(api_key, password),
        headers=headers,
        data=json.dumps(data)
    )
    response = json.loads(req.content)
    if req.status_code == 201:
        return response
    return req.status_code
