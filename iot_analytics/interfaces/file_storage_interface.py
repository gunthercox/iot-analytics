from .storage_interface import StorageInterface
from tinydb import TinyDB, Query
from datetime import datetime


class FileStorageInterface(StorageInterface):

    def initialize(self):
        self.storage = TinyDB('./db.json')

    def add(self, tracking_id, event_type, data):
        """
        Add an event object to storage.
        """
        if not self.can("write"):
            return False

        self.storage.insert({
            'id': tracking_id,
            'type': event_type,
            'date': datetime.now(),
            'data': data
        })

