class Serializer(object):

    def __init__(self):
        self.defaults = {}
        self.mapping = set()

        self.mapping.add(('device_id', 'device_id'))
        self.mapping.add(('type', 't'))

    def serialize(self, client, event):
        serialized = {}

        serialized['v'] = client.version
        serialized['tid'] = client.property_id
        serialized['cid'] = client.client_id
        serialized['cd'] = client.client_id

        for pair in self.mapping:
            local = pair[0]
            remote = pair[1]

            if local in self.defaults:
                serialized[remote] = event.data.get(
                    local,
                    self.defaults[local]
                )
            else:
                serialized[remote] = event.data.get(local)

            # Remove attribute from serialized data if value is none
            if serialized[remote] is None:
                serialized.pop(remote)

        return serialized

    def deserialize(self, event_data):
        pass


class EventSerializer(Serializer):

    def __init__(self):
        super(EventSerializer, self).__init__()

        self.mapping.add(('category', 'ec'))
        self.mapping.add(('action', 'ea'))
        self.mapping.add(('label', 'el'))
        self.mapping.add(('value', 'ev'))


class ErrorSerializer(Serializer):

    def __init__(self):
        super(ErrorSerializer, self).__init__()

        self.defaults['description'] = 'Exception'
        self.defaults['is_fatal'] = 0

        self.mapping.add(('type', 't'))
        self.mapping.add(('description', 'exd'))
        self.mapping.add(('is_fatal', 'exf'))

    def serialize(self, client, event):
        serialized = super(ErrorSerializer, self).serialize(client, event)

        serialized['t'] = 'exception'

        return serialized


class TimingSerializer(Serializer):

    def __init__(self):
        super(TimingSerializer, self).__init__()

        self.mapping.add(('category', 'utc'))
        self.mapping.add(('name', 'utv'))
        self.mapping.add(('time', 'utt'))
        self.mapping.add(('label', 'utl'))


class HitSerializer(Serializer):

    def __init__(self):
        super(HitSerializer, self).__init__()

        self.mapping.add(('hostname', 'dh'))
        self.mapping.add(('path', 'dp'))
        self.mapping.add(('title', 'dt'))

    def serialize(self, client, event):
        serialized = super(HitSerializer, self).serialize(client, event)

        serialized['t'] = 'pageview'

        return serialized
