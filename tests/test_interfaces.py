from unittest import TestCase
from iot_analytics.interfaces import FileStorageInterface


class TestStorageInterface(TestCase):

    def setUp(self):
        self.interface = FileStorageInterface()

    def test_can(self):
        self.assertTrue(self.interface.can("read"))
