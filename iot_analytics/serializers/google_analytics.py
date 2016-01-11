def serialize_event(client, event):
    serialized = {}

    serialized['t'] = 'event'
    serialized['v'] = client.version
    serialized['tid'] = client.property_id
    serialized['cid'] = client.client_id
    serialized['cd'] = client.client_id

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
    serialized = {}

    serialized['t'] = 'exception'
    serialized['v'] = client.version
    serialized['tid'] = client.property_id
    serialized['cid'] = client.client_id
    serialized['cd'] = client.client_id

    serialized['exd'] = event.data.get('description', 'Exception')
    serialized['exf'] = event.data.get('is_fatal', 0)

    return serialized
