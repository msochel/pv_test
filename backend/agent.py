# Internal modules
from views import get_handler


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
