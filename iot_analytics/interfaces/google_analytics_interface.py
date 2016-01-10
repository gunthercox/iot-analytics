from .storage_interface import StorageInterface
from iot_analytics.serializers import google_analytics


class GoogleAnalyticsInterface(StorageInterface):

    def __init__(self, property_id, client_id, version=1):
        super(GoogleAnalyticsInterface, self).__init__()

        self.property_id = property_id
        self.client_id = client_id
        self.version = version

    def initialize(self):

        # Remove the read permission
        self.permissions.remove('read')

    def serialize(self, client, obj):
        data = {
            'property_id': self.property_id,
            'client_id': self.client_id,
            'version': self.version
        }

        if obj.type is 'event':
            serializes_event = google_analytics.serialize_event(client, obj)
            data.update(serializes_event)

        return data        

    def add(self, event):
        """
        Add an event object to storage.
        """
        if not self.can('write'):
            return False

        data = {
            'id': event.property_id,
            'type': event.type
        }

        data.update(event.data)

        self.storage.insert(data)
