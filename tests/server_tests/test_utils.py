from unittest import TestCase
from iot_analytics.server import utils


class TestUtils(TestCase):

    def test_normalize_body_json(self):
        """
        Test that the correct data is returned
        when the request body is in json format.
        """
        content_type = 'application/x-www-form-urlencoded'
        request_body = 'category=button&action=pressed'
        data = utils.normalize_body(content_type, request_body)

        self.assertIn('category', data)
        self.assertIn('action', data)
        self.assertEqual(data['category'], 'button')
        self.assertEqual(data['action'], 'pressed')
        
    def test_normalize_body_urlencoded(self):
        """
        Test that the correct data is returned
        when the request body is urlencoded.
        """
        content_type = 'application/json'
        request_body = '{"category":"button","action":"pressed"}'
        data = utils.normalize_body(content_type, request_body)

        self.assertIn('category', data)
        self.assertIn('action', data)
        self.assertEqual(data['category'], 'button')
        self.assertEqual(data['action'], 'pressed')
