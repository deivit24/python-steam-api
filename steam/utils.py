from urllib.parse import urlencode


def buildUrlWithParams(url: str, key: str, params={}) -> str:
    encoded = urlencode(cleanDict(params))
    return (
        url + "?key=" + key
        if (len(encoded) == 0)
        else (url + "?key=" + key + "&" + encoded)
    )


def buildUrlWithParamsForSearch(url: str, search: str, params={}) -> str:
    encoded = urlencode(cleanDict(params))
    return (
        url + "?term=" + search
        if (len(encoded) == 0)
        else (url + "?term=" + search + "&" + encoded)
    )


def cleanDict(x: dict = {}) -> dict:
    result = {}
    for key in x:
        if x[key] is not None:
            # Check If List
            if isinstance(x[key], (list,)):
                result[key] = ",".join(x[key])
            # Check If Boolean
            elif isinstance(x[key], (bool)):
                if x[key] is True:
                    result[key] = "true"
                else:
                    result[key] = "false"
            # Everything Else (Strings/Numbers)
            else:
                result[key] = x[key]
    return result


def mergeDict(x: dict, y: dict) -> dict:
    z = cleanDict(x)
    z.update(cleanDict(y))
    return z


def retry(times, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param times: The number of times to repeat the wrapped function/method
    :type times: Int
    :param Exceptions: Lists of exceptions that trigger a retry attempt
    :type Exceptions: Tuple of Exceptions
    """
    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
                    )
                    attempt += 1
            return func(*args, **kwargs)
        return newfn
    return decorator