import requests

from IHRM import app


class EmployeeAPI:
    def __init__(self):
        self.add_url = app.BASE_URL + "/api/sys/user"
        self.update_url = app.BASE_URL + "/api/sys/user"
        self.delete_url = app.BASE_URL + "/api/sys/user"

    def add(self, header, data):
        return requests.post(self.add_url, json=data, headers=header)

    def update(self):
        pass

    def delete(self):
        pass
