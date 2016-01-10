from .storage_interface import StorageInterface
from tinydb import TinyDB, Query
from datetime import datetime


class FileStorageInterface(StorageInterface):

    def initialize(self):
        self.storage = TinyDB('./db.json')

    def add(self, event):
        """
        Add an event object to storage.
        """
        if not self.can("write"):
            return False

        self.storage.insert({
            'id': event.id,
            'type': event.type,
            'date': datetime.now(),
            'data': event.data
        })

