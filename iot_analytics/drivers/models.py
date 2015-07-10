from zorg.driver import Driver


class BaseAnalyticsDriver(Driver):
    """
    Driver containing basic commands
    used by all analytics drivers.
    """

    def __init__(self, options, connection):
        super(BaseAnalyticsDriver, self).__init__(options, connection)

        self.commands += ["send"]

    def send(self, **kwargs):
        # TODO: Throw not implemented exception.
        pass


class Event(BaseAnalyticsDriver):
    """
    Driver for generic events.
    """

    def __init__(self, options, connection):
        super(Event, self).__init__(options, connection)

        self.TYPE = 'event'

    def send(self, **kwargs):
        super(Event, self).send(**kwargs)

        details = {}

        category = kwargs.get("category", None)
        if category:
            details["ec"] = category

        action = kwargs.get("action", None)
        if action:
            details["ea"] = action

        label = kwargs.get("label", None)
        if label:
            details["el"] = label

        value = kwargs.get("value", 0)
        if value:
            details["ev"] = value

        return self.connection.http_send(self.TYPE, **details)


class Error(BaseAnalyticsDriver):
    """
    Driver for exception and error reporting.
    """

    def __init__(self, options, connection):
        super(Error, self).__init__(options, connection)

        self.TYPE = 'exception'

    def send(self, **kwargs):
        super(Error, self).send(**kwargs)

        details = {}

        description = kwargs.get("description", "Exception")
        details["exd"] = description # eg: IOException

        is_fatal = kwargs.get("is_fatal", 0)
        details["exf"] = is_fatal # eg: 1

        return self.connection.http_send(self.TYPE, **details)


class ApiResponseTime(BaseAnalyticsDriver):
    """
    Track multiple responses over time.
    Record the value of the amount of
    time taken to process and return a
    given response.
    """

    def __init__(self, options, connection):
        super(ApiResponseTime, self).__init__(options, connection)

        self.TYPE = 'timing'

    def send(self, **kwargs):
        super(ApiResponseTime, self).send(**kwargs)

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

        return self.connection.http_send(self.TYPE, **details)


class ApiHit(BaseAnalyticsDriver):

    def __init__(self):
        self.type = 'pageview'
        self.hostname = 'mydemo.com'
        self.page = '/api/blah'
        self.title = 'homepage'


class BatteryPerformance(BaseAnalyticsDriver):
    """
    Track the voltage level of the battery
    over time. Note when chatging and discharging.
    """
    pass


class Geolocation(BaseAnalyticsDriver):
    """
    Record the current coordinate of the
    robot at a give time.
    """
    pass
    # How to include this data?

