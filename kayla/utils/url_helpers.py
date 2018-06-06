import urlparse
import urllib


def build_url(url, query_params={}, clear_none=False):
    parts = urlparse.urlparse(url)
    scheme = parts.scheme or 'http'
    url_result = scheme + '://' + parts.netloc + parts.path
    query_dict = dict(urlparse.parse_qsl(parts.query))
    query_dict.update(query_params)

    if clear_none:
        params_dict = {k: v for k, v in query_dict.iteritems() if v is not None}
    else:
        params_dict = query_dict
    if any(params_dict):
        query_string = urllib.urlencode(params_dict)
        url_result = url_result + '?' + query_string

    if any(parts.fragment):
        url_result = url_result + '#' + parts.fragment

    return url_result


def build_query_string(params, order_by_key=False):
    """
    Build query string with format key1=value1&key2=value2...
    :param params: dictionary of parameters
    :param order_by_key: order params by keys
    :return: query string
    """
    if not isinstance(params, dict):
        params = dict(params)
    if order_by_key:
        params = sorted(params.items(), key=lambda val: val[0])
    return urllib.urlencode(params)
