from unittest import TestCase
from iot_analytics.apps.zorg.adaptors import GoogleAnalytics
from iot_analytics.apps.zorg.drivers import Event


class TestEvent(TestCase):

    def setUp(self):
        options = {
            "property_id": "UA-12573345-12",
            "client_id": "d944d45c-9c92-46a2-97be-9ba07d922227",
        }
        self.connection = GoogleAnalytics(options)
        self.driver = Event(options, self.connection)

    def test_send(self):
        response = self.driver.send()
        self.assertEqual(response.status_code, 200)
