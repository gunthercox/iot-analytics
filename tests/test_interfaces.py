from unittest import TestCase
from iot_analytics.interfaces import (
    FileStorageInterface,
    GoogleAnalyticsInterface
)


class TestFileStorageInterface(TestCase):

    def setUp(self):
        self.interface = FileStorageInterface()

    def test_can_write(self):
        self.assertTrue(self.interface.can('write'))

    def test_can_read(self):
        self.assertTrue(self.interface.can('read'))


class TestGoogleAnalyticsInterface(TestCase):

    def setUp(self):
        self.interface = GoogleAnalyticsInterface(
            property_id='UA-12573345-12',
            client_id='testing'
        )

    def test_can_write(self):
        self.assertTrue(self.interface.can('write'))

    def test_can_read(self):
        self.assertFalse(self.interface.can('read'))
