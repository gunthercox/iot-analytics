from tornado import escape


try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


def normalize_body(content_type, request_body):
    """
    Takes the content type and the request body as parameters.
    Returns a dictionary representation of the content.
    """
    if 'form-urlencoded' in content_type:
        parsed = urlparse.parse_qs(request_body)
        data = {}

        # Normalize the urldecoded data
        for p in parsed:
            data[p] = parsed[p][0]
    else:
        data = escape.json_decode(request_body)

    return data
