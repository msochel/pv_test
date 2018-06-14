# External libraries
import requests

# Internal libraries
from pprint import pprint
from methods_handler import get_handler


class Agent():
    def data_agent():
        page = 1
        while True:
            agents = get_handler(f'agents?per_page=3&page={page}')
            if agents:
                for agent in agents:
                    if agent['occasional'] != True:
                        yield {
                            'name': agent['contact']['name'],
                            'email': agent['contact']['email'],
                            '_id': agent['id'],
                            'created_at': agent['created_at'],
                            'updated_at': agent['updated_at']
                        }
                page += 1
            else:
                break


# for agent in Agent.all_agent():
#     pprint(agent)
