from .storage_interface import StorageInterface
from iot_analytics.serializers import google_analytics
import requests


class GoogleAnalyticsInterface(StorageInterface):

    def __init__(self, property_id, client_id, version=1):
        super(GoogleAnalyticsInterface, self).__init__()

        self.host = "http://www.google-analytics.com/collect"

        self.property_id = property_id
        self.client_id = client_id
        self.version = version

    def initialize(self):

        # Remove the read permission
        self.permissions.remove('read')

    def serialize(self, obj):

        if obj.type is 'event':
            return google_analytics.serialize_event(self, obj)

        if obj.type is 'error':
            return google_analytics.serialize_error(self, obj)

        if obj.type is 'timing':
            return google_analytics.serialize_timing(self, obj)

        if obj.type is 'hit':
            return google_analytics.serialize_hit(self, obj)

        return {}        

    def add(self, event):
        """
        Add an event object to storage.
        """
        if not self.can('write'):
            return False

        serialized = self.serialize(event)
        response = requests.post(self.host, data=serialized)

        response.json = serialized

        return response
