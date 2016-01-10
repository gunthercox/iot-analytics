from zorg.adaptor import Adaptor
from iot_analytics.interfaces import GoogleAnalyticsInterface
import requests


class GoogleAnalytics(Adaptor):

    def __init__(self, options):
        super(GoogleAnalytics, self).__init__(options)

        self.host = "http://www.google-analytics.com/collect"

        # Required parameters for each payload
        property_id = options.get("property_id", "UA-XXXX-Y")
        client_id = options.get("client_id", 555)
        version = options.get("version", 1)

        self.google_analytics = GoogleAnalyticsInterface(
            property_id, client_id, version
        )

    def http_send(self, event):
        """
        Sends a data payload to the data connection.
        """
        serialized = self.google_analytics.serialize(
            self.google_analytics,
            event
        )

        return requests.post(self.host, data=serialized)
