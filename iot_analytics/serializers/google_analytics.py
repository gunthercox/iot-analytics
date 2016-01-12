def serialize(client, event):
    serialized = {}

    serialized['v'] = client.version
    serialized['tid'] = client.property_id
    serialized['cid'] = client.client_id
    serialized['cd'] = client.client_id

    return serialized


def serialize_event(client, event):
    serialized = serialize(client, event)

    serialized['t'] = 'event'

    if 'device_id' in event.data:
        serialized['device_id'] = event.data.get('device_id')

    if 'category' in event.data:
        serialized['ec'] = event.data.get('category')

    if 'action' in event.data:
        serialized['ea'] = event.data.get('action')

    if 'label' in event.data:
        serialized['el'] = event.data.get('label')

    if 'value' in event.data:
        serialized['ev'] = event.data.get('value')

    return serialized


def serialize_error(client, event):
    serialized = serialize(client, event)

    serialized['t'] = 'exception'

    serialized['exd'] = event.data.get('description', 'Exception')
    serialized['exf'] = event.data.get('is_fatal', 0)

    return serialized


def serialize_timing(client, event):
    serialized = serialize(client, event)

    serialized['t'] = 'timing'

    if 'category' in event.data:
        serialized['utc'] = event.data.get('category')

    if 'name' in event.data:
        serialized['utv'] = event.data.get('name')

    if 'time' in event.data:
        serialized['utt'] = event.data.get('time')

    if 'label' in event.data:
        serialized['utl'] = event.data.get('label')

    return serialized


def serialize_hit(client, event):
    serialized = serialize(client, event)

    serialized['t'] = 'pageview'

    if 'hostname' in event.data:
        serialized['dh'] = event.data.get('hostname')

    if 'path' in event.data:
        serialized['dp'] = event.data.get('path')

    if 'title' in event.data:
        serialized['dt'] = event.data.get('title')

    return serialized
