import requests
from api.token import get_token


class Client:

    def __init__(self):
        self.base_url = 'https://api.github.com/'

        token = get_token()
        self.headers = {'Authorization': 'token ' + token}

    def get(self, path, params):
        response = requests.get(
            self.base_url + path,
            headers=self.headers,
            params=params
        ).json()

        return response
