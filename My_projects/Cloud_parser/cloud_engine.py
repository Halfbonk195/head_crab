import requests
import json

class Loginbot:
    """Парсит сайты с логином и паролем"""

    def __init__(self, data, login_url, headers=None):
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/90.0.4430.212 Safari/537.36'}
        self.data = data
        self.headers = headers
        self.login_url = login_url

    def parser(self, url):
        with requests.Session() as s:
            s.get(self.login_url)
            s.post(self.login_url, data=self.data, headers=self.headers)

            answer = s.get(url).text
            return answer

    def put(self, url, data):
        with requests.Session() as s:
            s.get(self.login_url)
            s.post(self.login_url, data=self.data, headers=self.headers)

            answer = s.put(url, json=data)
            return answer
