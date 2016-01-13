from .storage_interface import StorageInterface
from iot_analytics.serializers import google_analytics
import requests


class GoogleAnalyticsInterface(StorageInterface):

    def initialize(self, **kwargs):

        self.host = "http://www.google-analytics.com/collect"

        self.property_id = kwargs.get('property_id')
        self.client_id = kwargs.get('client_id')
        self.version = kwargs.get('version', 1)

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
