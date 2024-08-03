import json
import typing

from bs4 import BeautifulSoup
from requests import Response, request

from .client import Client
from .constants import API_APP_DETAILS_URL, API_APP_SEARCH_URL
from .utils import buildUrlWithParamsForSearch


class Apps:
    """Steam Apps API client"""

    def __init__(self, client: Client):
        """Constructor for Steam Apps class"""
        self.__client = client
        self.__search_url = API_APP_SEARCH_URL
        self.__app_details_url = API_APP_DETAILS_URL

    def get_app_details(self, app_id: int, country="US", filters: typing.Optional[str] = "basic") -> dict:
        """Obtains an apps details

        Args:
            app_id (int): App ID. For example 546560 (Half-Life-Alyx)
            country (str): ISO Country Code
            filters (str): list of keys to return, e.g. "name,platforms,price_overview". If you use multiple appids,
            you must set this parameter to "price_overview".
                The filter basic returns the following keys:
                    type
                    name
                    steam_appid
                    required_age
                    dlc
                    detailed_description
                    about_the_game
                    supported_languages
                    detailed_description
                    supported_languages
                    header_image
                    website
                    pc_requirements
                    mac_requirements
                    linux_requirements
                Any key names except those listed under basic are acceptable as filter values.
                Optional filters:
                    controller_support,
                    fullgame,
                    legal_notice,
                    developers,
                    demos,
                    price_overview,
                    metacritic,
                    categories,
                    genres,
                    screenshots,
                    movies,
                    recommendations,
                    achievements,
        """
        response = request(
            "get",
            self.__app_details_url,
            params={"appids": app_id, "cc": country, "filters": filters},
        )
        json_loaded_response = json.loads(response.text)
        return json_loaded_response

    def get_user_stats(self, steam_id: int, app_id: int) -> dict:
        """Obtains a user's stats for a specific app, includes only completed achievements
        along with app specific information

        Args:
            steam_id (int): Steam 64 ID
            app_id (int): App ID
        """
        response = self.__client.request(
            "get",
            "/ISteamUserStats/GetUserStatsForGame/v2/",
            params={"steamid": steam_id, "appid": app_id},
        )
        return response

    def get_user_achievements(self, steam_id: int, app_id: int, language: str = "en") -> dict:
        """Obtains information of the user's achievements in the app

        Args:
            steam_id (int): Steam 64 ID
            app_id (int): App ID
            language: (str) Abbriviated language
        """
        response = self.__client.request(
            "get",
            "/ISteamUserStats/GetPlayerAchievements/v1/",
            params={"steamid": steam_id, "appid": app_id, "l": language},
        )
        return response

    def file_service_get_details(
        self,
        key: str,
        publishedfileids: list[int],
        includetags: bool = True,
        includeadditionalpreviews: bool = True,
        includechildren: bool = True,
        includekvtags: bool = True,
        includevotes: bool = True,
        short_description: bool = True,
        includeforsaledata: bool = True,
        includemetadata: bool = True,
        language: typing.Optional[int] = None,
        return_playtime_stats: int = 30,
        appid: typing.Optional[int] = None,
        strip_description_bbcode: bool = True,
        desired_revision: typing.Optional[int] = None,
        includereactions: bool = False,
        admin_query: bool = True,
    ) -> dict:
        """Queries files with the Steamworks Web API

        Args:
            key (str): Steamworks Web API user authentication key.
            publishedfileids (List[int]): Set of published file IDs to retrieve details for.
            includetags (bool): If true, return tag information in the returned details.
            includeadditionalpreviews (bool): If true, return preview information in the returned details.
            includechildren (bool): If true, return children in the returned details.
            includekvtags (bool): If true, return key value tags in the returned details.
            includevotes (bool): If true, return vote data in the returned details.
            short_description (bool): If true, return a short description instead of the full description.
            includeforsaledata (bool): If true, return pricing data, if applicable.
            includemetadata (bool): If true, populate the metadata field.
            language (Optional[int]): Specifies the localized text to return. Defaults to English.
            return_playtime_stats (int): Return playtime stats for the specified number of days before today.
            appid (Optional[int]): App ID associated with the published files.
            strip_description_bbcode (bool): Strips BBCode from descriptions.
            desired_revision (Optional[int]): Return the data for the specified revision.
            includereactions (bool): If true, reactions to items will be returned.
            admin_query (bool): If true, return hidden items.
        """
        params = {
            "key": key,
            "includetags": includetags,
            "includeadditionalpreviews": includeadditionalpreviews,
            "includechildren": includechildren,
            "includekvtags": includekvtags,
            "includevotes": includevotes,
            "short_description": short_description,
            "includeforsaledata": includeforsaledata,
            "includemetadata": includemetadata,
            "language": language,
            "return_playtime_stats": return_playtime_stats,
            "appid": appid,
            "strip_description_bbcode": strip_description_bbcode,
            "desired_revision": desired_revision,
            "includereactions": includereactions,
            "admin_query": admin_query,
        }

        # Add published file IDs to parameters
        for index, file_id in enumerate(publishedfileids):
            params[f"publishedfileids[{index}]"] = file_id

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        response = self.__client.request("get", "/IPublishedFileService/GetDetails/v1/", params=params)

        return response

    # Is term meant to be any or a string, I'm not familiar enough with steam search so I'll leave it as is
    def search_games(self, term, country="US"):
        """Searches for games using the information given
        Args:
            term (Any): Search term
            country (str): ISO Country Code
        """
        url = self.search_url(term, country)
        result = request("get", url)
        html = self.__validator(result)

        # Decode the HTML content for Unicode escape sequences
        decoded_html = html.encode("utf-8").decode("unicode_escape")

        # Parse the decoded HTML with BeautifulSoup
        soup = BeautifulSoup(decoded_html, features="html.parser")
        links = soup.find_all("a")
        apps = []
        for link in links:
            if link.has_attr("data-ds-appid"):
                app = {}
                string_id = link["data-ds-appid"]
                href = link["href"].replace("\\", "").replace('"', "")
                app["id"] = [int(i) for i in string_id.replace("\\", "").replace('"', "").split(",")]
                app["link"] = href

                # Extracting the div elements and their content
                divs = link.find_all("div")
                for div in divs:
                    class_name = div.get("class")[0].strip('\\"')
                    if class_name == "match_name":
                        app["name"] = div.text
                    elif class_name == "match_price":
                        app["price"] = div.text
                    elif class_name == "match_img":
                        img_tag = div.find("img")
                        if img_tag and img_tag.has_attr("src"):
                            app["img"] = img_tag["src"].replace("\\", "").replace('"', "")

                apps.append(app)

        return {"apps": apps}

    # This should be a private method imo, I don't know how you would like to name them so I'll leave it as is
    # (Maybe change it to all caps since __search_url and __app_details_url are constants?)
    def search_url(self, search, country="US"):
        params = {"f": "games", "cc": country, "realm": 1, "l": "english"}
        result = buildUrlWithParamsForSearch((self.__search_url), search, params=params)
        return result

    def __validator(self, result: Response) -> typing.Union[str, dict]:
        try:
            body = json.dumps(result.text)
        except Exception:
            body = {}

        if isinstance(body, dict) and body.get("code", None) is not None:
            raise Exception(body.get("description"))
        elif result.status_code >= 400:
            raise Exception(" ".join([str(result.status_code), result.reason]))
        elif len(result.text) == 0:
            return "OK"
        else:
            return body
