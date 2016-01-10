class BaseEvent(object):

    def is_valid(self):
        """
        An account ID and an event type are required.
        """
        if self.id and self.type and self.type in EVENT_TYPES:
            return True

        return False

    def clean_data(self, data):
        """
        Removes any fields from the data that are not valid
        fields on the event object.
        """

        for item in data:
            if item not in self.fields:
                del data[item]

        return data


class Event(BaseEvent):
    """
    An event is something that happens.
    An example of an event may be something such as a button being pressed.
    """

    def __init__(self, tracking_id, event_type, data):
        self.id = tracking_id
        self.type = event_type

        self.fields = (
            'category',
            'action',
            'label',
            'value',
        )

        self.data = self.clean_data(data)


EVENT_TYPES = {
    'event': Event,
}


def get_model_for_type(event_type):
    from iot_analytics.exceptions import InvalidTypeException

    # Make sure that the type is valid
    if event_type not in EVENT_TYPES:
        raise InvalidTypeException()

    return EVENT_TYPES[event_type]
