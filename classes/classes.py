from abc import ABC, abstractmethod

import requests
from pprint import pprint


class Engine(ABC):
    def get_request(self):
        pass


class HeadHunterAPI(Engine):
    def get_request(self, keyword, page):
        headers = {
            "User-Agent": "TestApp/1.0(test@example.com)"
        }
        params = {
            "text": keyword,
            "page": page,
            "per_page": 100,
        }
        return requests.get("https://api.hh.ru/vacancies", params=params, headers=headers).json()["items"]

    def get_vacation(self, keyword, count=1000):
        pages = 10
        response = []
        for page in pages:
            print(page)
            values = self.get_request(keyword, page)
            pprint(values)
