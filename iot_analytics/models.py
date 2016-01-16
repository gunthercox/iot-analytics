class BaseEvent(object):

    def is_valid(self):
        """
        An account ID and an event type are required.
        """
        if self.property_id and self.type and self.type in EVENT_TYPES:
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

    def __init__(self, property_id, data):
        self.property_id = property_id
        self.type = 'event'

        self.fields = (
            'device_id',
            'category',
            'action',
            'label',
            'value',
        )

        self.data = self.clean_data(data)

        # Add the type to the data
        self.data['type'] = self.type


class Error(BaseEvent):

    def __init__(self, property_id, data):
        self.property_id = property_id
        self.type = 'error'

        self.fields = (
            'device_id',
            'description',
            'is_fatal',
        )

        self.data = self.clean_data(data)

        # Add the type to the data
        self.data['type'] = self.type


class Timing(BaseEvent):

    def __init__(self, property_id, data):
        self.property_id = property_id
        self.type = 'timing'

        self.fields = (
            'device_id',
            'category',
            'name',
            'time',
            'label',
        )

        self.data = self.clean_data(data)

        # Add the type to the data
        self.data['type'] = self.type


class ApiHit(BaseEvent):

    def __init__(self, property_id, data):
        self.property_id = property_id
        self.type = 'hit'

        self.fields = (
            'device_id',
            'hostname',
            'path',
            'title',
        )

        self.data = self.clean_data(data)

        # Add the type to the data
        self.data['type'] = self.type


EVENT_TYPES = {
    'event': Event,
    'error': Error,
    'timing': Timing,
    'hit': ApiHit
}


def get_model_for_type(event_type):
    from iot_analytics.exceptions import InvalidTypeException

    # Make sure that the type is valid
    if event_type not in EVENT_TYPES:
        raise InvalidTypeException()

    return EVENT_TYPES[event_type]
