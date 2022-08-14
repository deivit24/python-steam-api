import json

import typing
from requests import request, Response
from .client import Client
from .utils import buildUrlWithParamsForSearch
from bs4 import BeautifulSoup
from .constants import API_APP_DETAILS_URL, API_APP_SEARCH_URL


class Apps:
    """Steam Apps API client"""

    def __init__(self, client: Client):
        """Constructor for Steam Apps class"""
        self.__client = client
        self.__search_url = API_APP_SEARCH_URL
        self.__app_details_url = API_APP_DETAILS_URL

    def get_app_details(self, app_id: int) -> dict:
        response = request("get", self.__app_details_url, params={"appids": app_id})
        json_loaded_response = json.loads(response.text)
        return json.dumps(json_loaded_response)

    def get_user_stats(self, steam_id: int, app_id: int) -> dict:
        response = self.__client.request(
            "get",
            "/ISteamUserStats/GetUserStatsForGame/v2/",
            params={"steamid": steam_id, "appid": app_id},
        )
        return response

    def get_user_achievements(self, steam_id: int, app_id: int) -> dict:
        response = self.__client.request(
            "get",
            "/ISteamUserStats/GetPlayerAchievements/v1/",
            params={"steamid": steam_id, "appid": app_id},
        )
        return response

    def search_games(self, term):
        url = self.search_url(term)
        result = request("get", url)
        html = self.__validator(result)
        soup = BeautifulSoup(html)
        links = soup.find_all("a")
        apps = []
        for l in links:
            app = {}
            string_id = l["data-ds-appid"]
            href = l["href"].replace("\\", "").replace('"', "")
            app["id"] = int(string_id.replace("\\", "").replace('"', ""))
            app["link"] = href
            divs = l.select("div")
            for div in divs:
                if div["class"][0] == '\\"match_name\\"':
                    app["name"] = div.text
                if div["class"][0] == '\\"match_price\\"':
                    app["price"] = div.text
                if div["class"][0] == '\\"match_img\\"':
                    app["img"] = div.img["src"].replace("\\", "").replace('"', "")
            apps.append(app)

        return {"apps": apps}

    def search_url(self, search, country="US"):
        params = {"f": "games", "cc": country, "realm": 1, "l": "english"}
        result = buildUrlWithParamsForSearch((self.__search_url), search, params=params)
        return result

    def __validator(self, result: Response) -> typing.Union[str, dict]:
        try:
            body = json.dumps(result.text)
        except Exception:
            body = {}

        if type(body) is dict and body.get("code", None) is not None:
            raise Exception(body.get("description"))
        elif result.status_code >= 400:
            raise Exception(" ".join([str(result.status_code), result.reason]))
        elif len(result.text) == 0:
            return "OK"
        else:
            return body
