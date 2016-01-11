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
    """
    Driver for event tracking.
    """

    def send(self, **kwargs):
        from iot_analytics.models import Event as IOTEvent

        event = IOTEvent(
            self.connection.google_analytics.property_id,
            kwargs
        )

        return self.connection.http_send(event)


class Error(AnalyticDriver):
    """
    Driver for exception and error reporting.
    """

    def send(self, **kwargs):
        from iot_analytics.models import Error as IOTError

        error = IOTError(
            self.connection.google_analytics.property_id,
            kwargs
        )

        return self.connection.http_send(error)


class Timing(AnalyticDriver):
    """
    Record the value of the amount of time taken to
    process and return a given response.
    """

    def send(self, **kwargs):
        from iot_analytics.models import Timing as IOTTiming

        response_time = IOTTiming(
            self.connection.google_analytics.property_id,
            kwargs
        )

        return self.connection.http_send(response_time)


class ApiHit(AnalyticDriver):
    """
    Record the value of the amount of time taken to
    process and return a given response.
    """

    def send(self, **kwargs):
        from iot_analytics.models import ApiHit as IOTApiHit

        hit = IOTApiHit(
            self.connection.google_analytics.property_id,
            kwargs
        )

        return self.connection.http_send(hit)
