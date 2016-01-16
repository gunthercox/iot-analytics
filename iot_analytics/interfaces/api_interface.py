from .storage_interface import StorageInterface
import requests


class ApiInterface(StorageInterface):

    def initialize(self, **kwargs):

        self.host = kwargs.get("host", "http://localhost:4000")

    def add(self, event):
        print(event.data)
        response = requests.post(self.host, data=event.data)
        return response
