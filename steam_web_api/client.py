import json
import typing

import requests

from .constants import API_BASE_URL
from .utils import buildUrlWithParams, mergeDict, retry


class Client:
    """Streams API HTTP client"""

    def __init__(self, key: str = "", headers: dict = {}):
        """Constructor for TypeForm API client"""
        self.__headers = mergeDict(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            headers,
        )
        self.key = key

    @retry(times=3, exceptions=(ValueError, TypeError))
    def request(self, method: str, url: str, data: any = {}, params: dict = {}, headers={}) -> typing.Union[str, dict]:
        requestUrl = buildUrlWithParams((API_BASE_URL + url), self.key, params)
        requestHeaders = mergeDict(self.__headers, headers)
        requestData = json.dumps(data) if len(data.keys()) > 0 else ""
        result = requests.request(method, requestUrl, data=requestData, headers=requestHeaders)
        return self.__validator(result)

    def __validator(self, result: requests.Response) -> typing.Union[str, dict]:
        try:
            body = json.loads(result.text)
        except Exception:
            body = {}

        if isinstance(body, dict) and body.get("code", None) is not None:
            raise Exception(body.get("description"))
        elif result.status_code >= 400:
            raise Exception(" ".join([str(result.status_code), result.reason, result.text]))
        elif len(result.text) == 0:
            return "OK"
        else:
            return body
