import json
from typing import Union

from requests import request

from .client import Client
from .constants import API_APP_WISHLIST


class Users:
    """Steam Users API client"""

    def __init__(self, client: Client):
        """Constructor for Steam Users class"""
        self.__client = client
        self.__wishlist_url = API_APP_WISHLIST

    def search_user(self, search: str) -> dict:
        """Searches for exact match

        Args:
            search (str): steam user. For example 'the12thchairman'
        """
        search_response = self.__client.request(
            "get", "/ISteamUser/ResolveVanityURL/v1/", params={"vanityurl": search}
        )["response"]

        if search_response["success"] != 1:
            return search_response["message"]
        steam_id = search_response["steamid"]
        return self.get_user_details(steam_id)

    def get_user_details(self, steam_id: str, single=True) -> dict:
        """Gets user/player details by steam ID

        Args:
            steam_id (str): Steam 64 ID
            single (bool, optional): Gets one player. Defaults to True. When false, steam_id can be a string of steamids
            and delimited by a ','

        """
        if single:
            user_response = self.__client.request(
                "get",
                "/ISteamUser/GetPlayerSummaries/v2/",
                params={"steamids": steam_id},
            )["response"]
            if "players" in user_response and user_response["players"]:
                return {"player": user_response["players"][0]}
            else:
                return {"player": None}
        else:
            user_response = {"players": []}
            steam_ids = steam_id.split(",")
            for i in range(0, len(steam_ids), 100):
                batch_ids = steam_ids[i : i + 100]
                batch_response = self.__client.request(
                    "get",
                    "/ISteamUser/GetPlayerSummaries/v2/",
                    params={"steamids": ",".join(batch_ids)},
                )["response"]
                user_response["players"].extend(batch_response["players"])
            return user_response

    def get_user_friends_list(self, steam_id: str, enriched=True) -> dict:
        """Gets friend list of a user

        Args:
            steam_id (str): Steam 64 ID
            enriched (bool, optional): Enriches the response with user details. Defaults to True.
        """
        friends_list_response = self.__client.request(
            "get", "/ISteamUser/GetFriendList/v1/", params={"steamid": steam_id}
        )["friendslist"]
        if enriched:
            transform_friends = self._transform_friends(friends_list_response)
            return {"friends": transform_friends}
        else:
            return friends_list_response

    def get_user_recently_played_games(self, steam_id: str) -> dict:
        """Gets recently played games

        Args:
            steam_id (str): Steam 64 ID
        """
        response = self.__client.request(
            "get",
            "/IPlayerService/GetRecentlyPlayedGames/v1/",
            params={"steamid": steam_id},
        )["response"]
        return response

    def get_owned_games(self, steam_id: str, include_appinfo=True, includ_free_games=True) -> dict:
        """Gets all owned games of a user by steam id

        Args:
            steam_id (str): Steam 64 ID
            include_appinfo (bool, optional): Includes app/game info. Defaults to True.
            includ_free_games (bool, optional): Includes free games. Defaults to True.
        """
        params = {
            "steamid": steam_id,
            "include_appinfo": include_appinfo,
            "include_played_free_games": includ_free_games,
        }
        response = self.__client.request(
            "get",
            "/IPlayerService/GetOwnedGames/v1/",
            params=params,
        )["response"]
        return response

    def get_user_steam_level(self, steam_id: str) -> dict:
        """Gets user steam level

        Args:
            steam_id (str): Steam 64 ID
        """
        response = self.__client.request(
            "get",
            "/IPlayerService/GetSteamLevel/v1/",
            params={"steamid": steam_id},
        )["response"]
        return response

    def get_user_badges(self, steam_id: str) -> dict:
        """Gets user steam badges

        Args:
            steam_id (str): Steam 64 ID
        """
        response = self.__client.request(
            "get",
            "/IPlayerService/GetBadges/v1/",
            params={"steamid": steam_id},
        )["response"]
        return response

    def get_community_badge_progress(self, steam_id: str, badge_id: int) -> dict:
        """Gets user community badge progress

        Args:
            steam_id (str): Steam 64 ID
            badge_id (int): Badge ID
        """
        response = self.__client.request(
            "get",
            "/IPlayerService/GetCommunityBadgeProgress/v1",
            params={"steamid": steam_id, "badgeid": badge_id},
        )["response"]
        return response

    def get_account_public_info(self, steam_id: str) -> dict:
        """Gets account public info

        Args:
            steam_id (str): Steam 64 ID
        """
        response = self.__client.request(
            "get",
            "/IGameServersService/GetAccountPublicInfo/v1",
            params={"steamid": steam_id},
        )
        return response

    def get_player_bans(self, steam_id: str) -> dict:
        """Gets account bans info

        Args:
            steam_id (str): Steam 64 ID
        """
        response = self.__client.request(
            "get",
            "/ISteamUser/GetPlayerBans/v1",
            params={"steamids": steam_id},
        )
        return response

    def _transform_friends(self, friends_list: dict) -> dict:
        friend_steam_ids = [friend["steamid"] for friend in friends_list["friends"]]
        friends = self.get_user_details(",".join(friend_steam_ids), False)["players"]
        for f in friends:
            found = next(item for item in friends_list["friends"] if item["steamid"] == f["steamid"])
            f["relationship"] = found["relationship"]
            f["friend_since"] = found["friend_since"]

        return friends

    def get_steamid(self, vanity: str) -> dict:
        """Get steamid64 from vanity URL

        Args:
            vanity (str): Vanity URL
        """
        response = self.__client.request(
            "get",
            "/ISteamUser/ResolveVanityURL/v1",
            params={"vanityurl": vanity},
        )["response"]
        return response

    def get_profile_wishlist(self, steam_id: str) -> Union[dict, list]:
        wishlist_profile_url = f"{self.__wishlist_url}"
        response = request(
            "get",
            wishlist_profile_url,
            params={"steamid": steam_id},
        )
        json_loaded_response = json.loads(response.text)
        does_no_exists = json_loaded_response.get("success", None)
        # This api is weird. If its successful, it returns a dict with the values
        # if its not successful it returns a dict with key called success with the value of 2.
        # This means the user does not have a wishwish. This is a, what I have doing if i
        # just returning an empty list
        if does_no_exists:
            return []
        return json_loaded_response["response"]["items"]

    def get_shared_games(self, steam_id: str, token: str, include_owned: bool = False) -> dict:
        """Gets shared games from family library. This is an undocumented API endpoint.

        Args:
            steam_id (str): Steam 64 ID
            token (str): Steam access token (can be fetched from https://store.steampowered.com/pointssummary/ajaxgetasyncconfig)
        """
        # The parameter include_own needs to be set to get all shared games. Apart from its name, it does not mean to get games the user owns.
        response = self.__client.request(
            "get",
            "/IFamilyGroupsService/GetSharedLibraryApps/v1",
            params={
                "steamids": steam_id,
                "access_token": token,
                "family_groupid": 0,
                "include_own": 1,
                "include_non_games": 0,
                "include_excluded": 0,
                "include_free": 0,
            },
        )["response"]
        if not include_owned:
            response["apps"] = [game for game in response["apps"] if steam_id not in game["owner_steamids"]]
        # Filter out family-excluded games like MMO/MP games and delisted games.
        # These games are usually not excluded by the include_excluded or include_free parameters (but still unavailable to share)
        response["apps"] = [game for game in response["apps"] if game["exclude_reason"] == 0]
        return response
