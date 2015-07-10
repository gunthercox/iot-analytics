from zorg.adaptor import Adaptor


class IntelIOTAnalytics(Adaptor):
    """
    https://software.intel.com/en-us/intel-iot-platforms-getting-started-cloud-analytics
    """

    def __init__(self, options):
        super(IntelIOTAnalytics, self).__init__(options)

        self.id = options.get("id", "")
