from zorg.driver import Driver


class AnalyticDriver(Driver):
    """
    Driver containing basic commands used by all analytics drivers.
    """

    def __init__(self, options, connection):
        super(AnalyticDriver, self).__init__(options, connection)

        self.commands += ['send']

    def send(self, **kwargs):
        raise Exception("This method needs to be implemented by a child class")


class Event(AnalyticDriver):

    def send(self, **kwargs):
        from iot_analytics.models import Event as IOTEvent

        event = IOTEvent(self.connection.google_analytics.property_id, kwargs)

        return self.connection.http_send(event)


class Error(AnalyticDriver):
    """
    Driver for exception and error reporting.
    """

    def send(self, **kwargs):
        TYPE = 'exception'
        details = {}

        description = kwargs.get("description", "Exception")
        details["exd"] = description # eg: IOException

        is_fatal = kwargs.get("is_fatal", 0)
        details["exf"] = is_fatal # eg: 1

        return self.connection.http_send(TYPE, **details)


class ApiResponseTime(AnalyticDriver):
    """
    Track multiple responses over time.
    Record the value of the amount of
    time taken to process and return a
    given response.
    """

    def send(self, **kwargs):
        TYPE = 'timing'
        details = {}

        timing_category = kwargs.get("timing_category", None)
        if timing_category:
            details["utc"] = timing_category # eg: 'jsonLoader'

        timing_variable = kwargs.get("timing_variable", None)
        if timing_variable:
            details["utv"] = timing_variable # eg: 'load'

        time = kwargs.get("time", None)
        if time:
            details["utt"] = time # eg: '5000'

        timing_label = kwargs.get("timing_label", None)
        if timing_label:
            details["utt"] = timing_label # eg: 'jQuery'

        return self.connection.http_send(TYPE, **details)


class ApiHit(AnalyticDriver):

    def send(self, **kwargs):
        type = 'pageview'
        hostname = 'mydemo.com'
        page = '/api/blah'
        title = 'homepage'


class BatteryPerformance(AnalyticDriver):
    """
    Track the voltage level of the battery
    over time. Note when charging and discharging.
    """

    def send(self, **kwargs):
        pass


class Geolocation(AnalyticDriver):
    """
    Record the current coordinate of the robot at a give time.
    """

    def send(self, **kwargs):
        pass

