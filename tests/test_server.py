from tornado.testing import AsyncHTTPTestCase
from iot_analytics.server import server
import tornado.escape

class ApiServerTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return server.make_app()

    def test_get(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)

    def test_post_valid_data(self):
        data = tornado.escape.json_encode(
            {'x':'y'}
        )
        response = self.fetch('/', method="POST", body=data)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, '')
