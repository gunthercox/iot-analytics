class BaseEvent(object):

    def is_valid(self):
        """
        An account ID and an event type are required.
        """
        if self.id and self.type and self.type in EVENT_TYPES:
            return True

        return False


class Event(BaseEvent):
    """
    An event is something that happens.
    An example of an event may be something such as a button being pressed.
    """

    def __init__(self, tracking_id, event_type, data):
        self.id = tracking_id
        self.type = event_type
        self.data = data

        self.fields = (
            'category',
            'action',
            'label',
            'value',
        )


EVENT_TYPES = {
    'event': Event,
}


def get_model_for_type(event_type):

    # TODO: Handle case that type is not valid

    return EVENT_TYPES[event_type]
