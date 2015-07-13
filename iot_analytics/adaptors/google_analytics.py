from zorg.adaptor import Adaptor
import requests


class GoogleAnalytics(Adaptor):

    def __init__(self, options):
        super(GoogleAnalytics, self).__init__(options)

        self.host = "http://www.google-analytics.com/collect"

        # Required parameters for each payload
        self._version = options.get("version", 1)
        self._property_id = options.get("property_id", "UA-XXXX-Y")
        self._client_id = options.get("client_id", 555)

    def serialize(self, **kwargs):
        serialized = kwargs

        serialized["v"] = self._version
        serialized["tid"] = self._property_id
        serialized["cid"] = self._client_id

        return serialized

    def http_send(self, event_type, **kwargs):
        """
        Sends a data payload to the data connection.
        """
        serialized = self.serialize(**kwargs)

        serialized["t"] = event_type

        print "serialized", serialized

        return requests.post(self.host, data=serialized)

