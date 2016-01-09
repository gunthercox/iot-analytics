from tornado_cors import CorsMixin
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado import escape


class MainHandler(CorsMixin, RequestHandler):

    def initialize(self, database):
        self.database = database

    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write({})

    def post(self):
        self.set_header("Content-Type", "application/json")

        data = escape.json_decode(self.request.body)

        # Get the tracking id from the request
        tracking_id = data.pop("id", None)

        # Get the type from the request
        event_type = data.pop("type", None)

        if tracking_id and event_type:
            self.database.add(tracking_id, event_type, data)

def make_database():
    from iot_analytics.interfaces import FileStorageInterface
    return FileStorageInterface()

def make_app():
    return Application([
       (r"/", MainHandler, dict(database=make_database())),
    ])

if __name__ == "__main__":
    application = make_app()
    application.listen(4000)
    IOLoop.instance().start()
