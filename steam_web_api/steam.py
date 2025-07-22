from .apps import Apps
from .client import Client
from .users import Users


class Steam:
    """Steam API client"""

    def __init__(self, key: str = "", headers: dict = {}):
        """Constructor for Steam API client"""
        client = Client(key, headers=headers)
        self.__users = Users(client)
        self.__apps = Apps(client)

    @property
    def users(self) -> Users:
        return self.__users

    @property
    def apps(self) -> Apps:
        return self.__apps
