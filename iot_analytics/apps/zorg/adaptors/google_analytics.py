from zorg.adaptor import Adaptor
import requests


class GoogleAnalytics(Adaptor):

    def __init__(self, options):
        super(GoogleAnalytics, self).__init__(options)

        self.host = "http://www.google-analytics.com/collect"

        # Required parameters for each payload
        self.version = options.get("version", 1)
        self.property_id = options.get("property_id", "UA-XXXX-Y")
        self.client_id = options.get("client_id", 555)

    def serialize(self, event, **kwargs):
        serialized = {}

        serialized["t"] = event.TYPE
        serialized["v"] = self.version
        serialized["tid"] = self.property_id
        serialized["cid"] = self.client_id

        if event.device_id:
            serialized["device_id"] = self.device_id

        if "category" in kwargs:
            serialized["ec"] = kwargs.get("category")

        if "action" in kwargs:
            serialized["ea"] = kwargs.get("action")

        if "label" in kwargs:
            serialized["el"] = kwargs.get("label")

        if "value" in kwargs:
            serialized["ev"] = kwargs.get("value")

        return serialized

    def deserialize(self, event):
        pass

    def http_send(self, event, **kwargs):
        """
        Sends a data payload to the data connection.
        """
        serialized = self.serialize(event, **kwargs)

        return requests.post(self.host, data=serialized)

    def servo_write(self, pin, degrees):
        pass

    def digital_write(self, pin_number, value):
        pass

    def digital_read(self, pin_number):
        value = None
        pass

    def pwm_write(self, pin_number, value, period):
        pass

    def analog_read(self, pin_number):
        pass

    def i2c_write(self, pin_number, address, register, data):
        pass

    def i2c_read(self, pin_number, address, register):
        data = None
        pass

