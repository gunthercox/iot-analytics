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
            serializer = google_analytics.EventSerializer()
            return serializer.serialize(self, obj)

        if obj.type is 'error':
            serializer = google_analytics.ErrorSerializer()
            return serializer.serialize(self, obj)

        if obj.type is 'timing':
            serializer = google_analytics.TimingSerializer()
            return serializer.serialize(self, obj)

        if obj.type is 'hit':
            serializer = google_analytics.HitSerializer()
            return serializer.serialize(self, obj)

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
