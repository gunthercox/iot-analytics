from zorg.adaptor import Adaptor
from iot_analytics.interfaces import GoogleAnalyticsInterface


class GoogleAnalytics(Adaptor):

    def __init__(self, options):
        super(GoogleAnalytics, self).__init__(options)

        # Required parameters for each payload
        property_id = options.get("property_id", "UA-XXXX-Y")
        client_id = options.get("client_id", '555')

        self.google_analytics = GoogleAnalyticsInterface(
            property_id=property_id,
            client_id=client_id
        )

    def http_send(self, event):
        """
        Sends a data payload to the data connection.
        """
        return self.google_analytics.add(event)
