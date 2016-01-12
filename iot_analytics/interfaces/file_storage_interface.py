from .storage_interface import StorageInterface
from tinydb import TinyDB, Query


class FileStorageInterface(StorageInterface):

    def initialize(self):
        self.storage = TinyDB('./db.json')

    def timestamp(self):
        import datetime
        import json

        encoding = lambda obj: (
            obj.isoformat()
            if isinstance(obj, datetime.datetime)
            or isinstance(obj, datetime.date)
            else None
        )
        return json.dumps({'date': datetime.datetime.now()}, default=encoding)

    def add(self, event):
        """
        Add an event object to storage.
        """
        if not self.can("write"):
            return False

        data = {
            'id': event.property_id,
            'type': event.type,
            'date': self.timestamp()
        }

        data.update(event.data)

        self.storage.insert(data)
