# Get Started

## Installation

`pip install python-steam-api`

## Create Steam API web key

[Steam API Web key](https://steamcommunity.com/dev/apikey)

Follow instructions to get API Key

# Set up your environment variable

To create an environment variable in Python, you can utilize the os module. Use os.environ to access and modify environment variables. To accommodate different operating systems, check the documentation or resources specific to each OS for instructions on setting environment variables. For example, on Windows, you can use the Command Prompt or PowerShell, while on Unix-based systems like Linux or macOS, you can modify configuration files or use terminal commands like export.

# Basic Usage

### Searching for a user

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)

steam.users.search_user("the12thchairman")
```

Response

```json
{
  "player": {
    "steamid": "76561198995017863",
    "communityvisibilitystate": 3,
    "profilestate": 1,
    "personaname": "The12thChairman",
    "profileurl": "https://steamcommunity.com/id/the12thchairman/",
    "avatar": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6.jpg",
    "avatarmedium": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6_medium.jpg",
    "avatarfull": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6_full.jpg",
    "avatarhash": "427ef7d5f8ad7b21678f69bc8afc95786cf38fe6",
    "lastlogoff": 1659923870,
    "personastate": 1,
    "primaryclanid": "103582791429521408",
    "timecreated": 1570311509,
    "personastateflags": 0,
    "loccountrycode": "US"
  }
}
```

### Getting User details by steam id

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_details("76561198995017863")
```

Response

```json
{
  "player": {
    "steamid": "76561198995017863",
    "communityvisibilitystate": 3,
    "profilestate": 1,
    "personaname": "The12thChairman",
    "profileurl": "https://steamcommunity.com/id/the12thchairman/",
    "avatar": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6.jpg",
    "avatarmedium": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6_medium.jpg",
    "avatarfull": "https://avatars.akamai.steamstatic.com/427ef7d5f8ad7b21678f69bc8afc95786cf38fe6_full.jpg",
    "avatarhash": "427ef7d5f8ad7b21678f69bc8afc95786cf38fe6",
    "lastlogoff": 1659923870,
    "personastate": 1,
    "primaryclanid": "103582791429521408",
    "timecreated": 1570311509,
    "personastateflags": 0,
    "loccountrycode": "US"
  }
}
```

### Getting Friends List

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_friends_list("76561198995017863")
```

Response

```json
{
  "friends": [
    {
      "steamid": "76561198164668273",
      "communityvisibilitystate": 3,
      "profilestate": 1,
      "personaname": "ProToType",
      "profileurl": "https://steamcommunity.com/id/bruuitssam/",
      "avatar": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg",
      "avatarmedium": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_medium.jpg",
      "avatarfull": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg",
      "avatarhash": "fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb",
      "lastlogoff": 1659791200,
      "personastate": 3,
      "realname": "Samuel chance",
      "primaryclanid": "103582791429521408",
      "timecreated": 1416698360,
      "personastateflags": 0,
      "loccountrycode": "US",
      "relationship": "friend",
      "friend_since": 1634692088
    },
    {
      "steamid": "76561198040366189",
      "communityvisibilitystate": 3,
      "profilestate": 1,
      "personaname": "\u2654 Regular Tetragon",
      "commentpermission": 1,
      "profileurl": "https://steamcommunity.com/id/regulartetragon/",
      "avatar": "https://avatars.akamai.steamstatic.com/85ee384bec86399cc79728cbde046516fa704b23.jpg",
      "avatarmedium": "https://avatars.akamai.steamstatic.com/85ee384bec86399cc79728cbde046516fa704b23_medium.jpg",
      "avatarfull": "https://avatars.akamai.steamstatic.com/85ee384bec86399cc79728cbde046516fa704b23_full.jpg",
      "avatarhash": "85ee384bec86399cc79728cbde046516fa704b23",
      "lastlogoff": 1659834670,
      "personastate": 0,
      "realname": "Vincent Mattingly",
      "primaryclanid": "103582791435763797",
      "timecreated": 1302294837,
      "personastateflags": 0,
      "relationship": "friend",
      "friend_since": 1649989273
    },
    {
      "steamid": "76561198030124562",
      "communityvisibilitystate": 3,
      "profilestate": 1,
      "personaname": "Robz",
      "profileurl": "https://steamcommunity.com/profiles/76561198030124562/",
      "avatar": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg",
      "avatarmedium": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_medium.jpg",
      "avatarfull": "https://avatars.akamai.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg",
      "avatarhash": "fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb",
      "lastlogoff": 1659320144,
      "personastate": 1,
      "primaryclanid": "103582791429521408",
      "timecreated": 1283739538,
      "personastateflags": 0,
      "relationship": "friend",
      "friend_since": 1634692171
    }
  ]
}
```

#### Getting Friends List *(flat version)*

For frequent friend list queries, you can disable enrichment to reduce the number of requests sent to the Steam Web API.

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_friends_list("76561198995017863", enriched=False)
```

Response

```json
{
  "friends": [
    {
      "friend_since": 1634692088,
      "relationship": "friend",
      "steamid": "76561198164668273"
    },
    {
      "friend_since": 1649989273,
      "relationship": "friend",
      "steamid": "76561198040366189"
    },
    {
      "friend_since": 1634692171,
      "relationship": "friend",
      "steamid": "76561198030124562"
    }
  ]
}
```

### Getting Users Recently Played Games

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_recently_played_games("76561198995017863")
```

### Getting User Owned Games

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_owned_games("76561198995017863")
```

### Getting User Shared Games / Family Library

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")
ACCESS_TOKEN = os.environ.get("STEAM_ACCESS_TOKEN")

steam = Steam(KEY)

# arguments: steamid, token, include_owned (default: False)
user = steam.users.get_shared_games("76561198995017863", ACCESS_TOKEN, include_owned=True)
```

### Getting User Steam Level

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_steam_level("76561198995017863")
```

### Getting User Badges

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_badges("76561198995017863")
```

### Getting Community Badge Progress

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid, badgeid
user = steam.users.get_community_badge_progress("<steam_id>", "<badge_id>")
```

### Getting User Public Account

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_account_public_info("<steam_id>")
```

### Searching for Games

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: search
user = steam.apps.search_games("terr")
```

Response

```json
{
  "apps": [
    {
      "id": 105600,
      "link": "https://store.steampowered.com/app/105600/Terraria/?snr=1_7_15__13",
      "name": "Terraria",
      "img": "https://cdn.akamai.steamstatic.com/steam/apps/105600/capsule_sm_120.jpg?t=1590092560",
      "price": "$9.99"
    },
    {
      "id": 1202130,
      "link": "https://store.steampowered.com/app/1202130/Starship_Troopers_Terran_Command/?snr=1_7_15__13",
      "name": "Starship Troopers: Terran Command",
      "img": "https://cdn.akamai.steamstatic.com/steam/apps/1202130/capsule_sm_120.jpg?t=1657104501",
      "price": "$29.99"
    },
    {
      "id": 1176470,
      "link": "https://store.steampowered.com/app/1176470/Terra_Invicta/?snr=1_7_15__13",
      "name": "Terra Invicta",
      "img": "https://cdn.akamai.steamstatic.com/steam/apps/1176470/capsule_sm_120.jpg?t=1659933796",
      "price": ""
    },
    {
      "id": 1945600,
      "link": "https://store.steampowered.com/app/1945600/The_Riftbreaker_Metal_Terror/?snr=1_7_15__13",
      "name": "The Riftbreaker: Metal Terror",
      "img": "https://cdn.akamai.steamstatic.com/steam/apps/1945600/capsule_sm_120.jpg?t=1659109312",
      "price": "$9.99"
    },
    {
      "id": 285920,
      "link": "https://store.steampowered.com/app/285920/TerraTech/?snr=1_7_15__13",
      "name": "TerraTech",
      "img": "https://cdn.akamai.steamstatic.com/steam/apps/285920/capsule_sm_120.jpg?t=1644900341",
      "price": "$24.99"
    }
  ]
}
```

### App/Game details

This call does not require a Steam API Key

#### Parameters:

- `app_id` (int): The unique App ID of the app you want to retrieve details for. For example, 105600 corresponds to "Terraria"
  i
- `country` (str): An optional parameter representing the ISO Country Code. The default value is "US."

- `filters` (str): An optional parameter that allows you to specify a list of keys to return in the app details. If not provided, it defaults to "basic." The available filter options include:

- `basic` (Default): Returns essential information like type, name, steam_appid, required_age, is_free, dlc, detailed_description, short_description, about_the_game, supported_languages, header_image, website, pc_requirements, mac_requirements, and linux_requirements.

- Optional filters (Specify one or more of these as a comma-separated string):
  - controller_support
  - dlc
  - fullgame
  - legal_notice
  - developers
  - demos
  - price_overview
  - metacritic
  - categories
  - genres
  - screenshots
  - movies
  - recommendations
  - achievements
    Response

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

terraria_app_id = 105600
steam = Steam(KEY)

# arguments: app_id
user = steam.apps.get_app_details(terraria_app_id)

```

```json
{
  "105600": {
    "success": true,
    "data": {
      "type": "game",
      "name": "Terraria",
      "steam_appid": 105600,
      "required_age": 0,
      "is_free": false,
      "controller_support": "full",
      "dlc": [409210, 1323320],
      "detailed_description": "Dig, Fight, Explore, Build:  The very world is at your fingertips as you fight for survival, fortune, and glory.   Will you delve deep into cavernous expanses in search of treasure and raw materials with which to craft ever-evolving gear, machinery, and aesthetics?   Perhaps you will choose instead to seek out ever-greater foes to test your mettle in combat?   Maybe you will decide to construct your own city to house the host of mysterious allies you may encounter along your travels? <br><br>In the World of Terraria, the choice is yours!<br><br>Blending elements of classic action games with the freedom of sandbox-style creativity, Terraria is a unique gaming experience where both the journey and the destination are completely in the player’s control.   The Terraria adventure is truly as unique as the players themselves!  <br><br>Are you up for the monumental task of exploring, creating, and defending a world of your own?  <br><br>\t\t\t\t\t\t\t<strong>Key features:</strong><br>\t\t\t\t\t\t\t<ul class=\"bb_ul\"><li>Sandbox Play<br>\t\t\t\t\t\t\t</li><li> Randomly generated worlds<br>\t\t\t\t\t\t\t</li><li>Free Content Updates<br>\t\t\t\t\t\t\t</li></ul>",
      "about_the_game": "Dig, Fight, Explore, Build:  The very world is at your fingertips as you fight for survival, fortune, and glory.   Will you delve deep into cavernous expanses in search of treasure and raw materials with which to craft ever-evolving gear, machinery, and aesthetics?   Perhaps you will choose instead to seek out ever-greater foes to test your mettle in combat?   Maybe you will decide to construct your own city to house the host of mysterious allies you may encounter along your travels? <br><br>In the World of Terraria, the choice is yours!<br><br>Blending elements of classic action games with the freedom of sandbox-style creativity, Terraria is a unique gaming experience where both the journey and the destination are completely in the player’s control.   The Terraria adventure is truly as unique as the players themselves!  <br><br>Are you up for the monumental task of exploring, creating, and defending a world of your own?  <br><br>\t\t\t\t\t\t\t<strong>Key features:</strong><br>\t\t\t\t\t\t\t<ul class=\"bb_ul\"><li>Sandbox Play<br>\t\t\t\t\t\t\t</li><li> Randomly generated worlds<br>\t\t\t\t\t\t\t</li><li>Free Content Updates<br>\t\t\t\t\t\t\t</li></ul>",
      "short_description": "Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game. Four Pack also available!",
      "supported_languages": "English, French, Italian, German, Spanish - Spain, Polish, Portuguese - Brazil, Russian, Simplified Chinese",
      "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/105600/header.jpg?t=1666290860",
      "capsule_image": "https://cdn.akamai.steamstatic.com/steam/apps/105600/capsule_231x87.jpg?t=1666290860",
      "capsule_imagev5": "https://cdn.akamai.steamstatic.com/steam/apps/105600/capsule_184x69.jpg?t=1666290860",
      "website": "http://www.terraria.org/",
      "pc_requirements": {
        "minimum": "<h2 class=\"bb_tag\"><strong>REQUIRED</strong></h2><ul class=\"bb_ul\"><li><strong>OS: Windows Xp, Vista, 7, 8/8.1, 10</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: 2.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 2.5GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 128mb Video Memory, capable of Shader Model 2.0+</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>DirectX®: 9.0c or Greater</strong> \t<br>\t\t\t\t\t\t\t\t\t</li></ul>",
        "recommended": "<h2 class=\"bb_tag\"><strong>RECOMMENDED</strong></h2><ul class=\"bb_ul\"><li><strong>OS: Windows 7, 8/8.1, 10</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: Dual Core 3.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 4GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 256mb Video Memory, capable of Shader Model 2.0+</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>DirectX®: 9.0c or Greater</strong> \t<br>\t\t\t\t\t\t\t\t\t</li></ul>"
      },
      "mac_requirements": {
        "minimum": "<h2 class=\"bb_tag\"><strong>REQUIRED</strong></h2><ul class=\"bb_ul\"><li><strong>OS: OSX 10.9.5 - 10.11.6</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: 2.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 2.5GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 128mb Video Memory, capable of OpenGL 3.0+ support (2.1 with ARB extensions acceptable</strong> <br>\t\t\t\t\t\t\t\t\t</li></ul>",
        "recommended": "<h2 class=\"bb_tag\"><strong>RECOMMENDED</strong></h2><ul class=\"bb_ul\"><li><strong>OS: OSX 10.9.5 - 10.11.6</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: Dual Core 3.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 4GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 256mb Video Memory, capable of OpenGL 3.0+ support (2.1 with ARB extensions acceptable</strong> <br>\t\t\t\t\t\t\t\t\t</li></ul>"
      },
      "linux_requirements": {
        "minimum": "<h2 class=\"bb_tag\"><strong>REQUIRED</strong></h2>LINUX<br><ul class=\"bb_ul\"><li><strong>OS: Ubuntu 14.04 LTS</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: 2.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 2.5GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 128mb Video Memory, capable of OpenGL 3.0+ support (2.1 with ARB extensions acceptable</strong> <br>\t\t\t\t\t\t\t\t\t</li></ul>",
        "recommended": "<h2 class=\"bb_tag\"><strong>RECOMMENDED</strong></h2>LINUX<br><ul class=\"bb_ul\"><li><strong>OS: Ubuntu 14.04 LTS</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Processor: Dual Core 3.0 Ghz</strong> <br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Memory: 4GB</strong><br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Hard Disk Space: 200MB </strong> \t<br>\t\t\t\t\t\t\t\t\t\t</li><li><strong>Video Card: 256mb Video Memory, capable of OpenGL 3.0+ support (2.1 with ARB extensions acceptable</strong> <br>\t\t\t\t\t\t\t\t\t</li></ul>"
      }
    }
  }
}
```

### Getting user app stats

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steam_id, app_id
user = steam.apps.get_user_stats("<steam_id>", "<app_id>")
```

### Getting user app achievements

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steam_id, app_id
user = steam.apps.get_user_achievements("<steam_id>", "<app_id>")
```

### Getting user ban status

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steam_id
user = steam.users.get_player_bans("<steam_id>")
```

```json
{
  "players": [
    {
      "SteamId": "76561198079362196",
      "CommunityBanned": false,
      "VACBanned": false,
      "NumberOfVACBans": 0,
      "DaysSinceLastBan": 0,
      "NumberOfGameBans": 0,
      "EconomyBan": "none"
    }
  ]
}
```

### Retrieves information about a set of published files.

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

key = <access_key>
# Can be multiple publish file ids
file_ids = [2086515808]


publishedfiledetails = steam.apps.file_service_get_details(
    key=key, publishedfileids=file_ids, includevotes=True
)
```

```python
{
    "response": {
        "publishedfiledetails": [
            {
                "result": 1,
                "publishedfileid": "2086515808",
                "creator": "76561198021181972",
                "creator_appid": 4000,
                "consumer_appid": 4000,
                "consumer_shortcutid": 0,
                "filename": "",
                "file_size": "77837190",
                "preview_file_size": "542105",
                "preview_url": "https://steamuserimages-a.akamaihd.net/ugc/1027328686644128049/6BBC8D5C3F8230DBAA5BACA9F43936E31B3C78D6/",
                "url": "",
                "hcontent_file": "8253646490380086716",
                "hcontent_preview": "1027328686644128049",
                "title": "TTT Windmill in the sky",
                "short_description": "Updated 18th May 2020 Fragments of land have drifted together to form a new tranquil land, floating way above the cities. While the gardens are peaceful, the wrong step may result in someone disappearing into the clouds. Feedback is greatly appreciated! No",
                "time_created": 1588735858,
                "time_updated": 1589755683,
                "visibility": 0,
                "flags": 5632,
                "workshop_file": False,
                "workshop_accepted": False,
                "show_subscribe_all": False,
                "num_comments_public": 67,
                "banned": False,
                "ban_reason": "",
                "banner": "76561197960265728",
                "can_be_deleted": True,
                "app_name": "Garry's Mod",
                "file_type": 0,
                "can_subscribe": True,
                "subscriptions": 19184,
                "favorited": 401,
                "followers": 0,
                "lifetime_subscriptions": 31670,
                "lifetime_favorited": 474,
                "lifetime_followers": 0,
                "lifetime_playtime": "0",
                "lifetime_playtime_sessions": "0",
                "views": 9468,
                "num_children": 0,
                "num_reports": 0,
                "previews": [
                    {
                        "previewid": "19122426",
                        "sortorder": 10,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074141/D656F3253B4BDAB6205F5182EFD4AFB2C4989741/",
                        "size": 396048,
                        "filename": "20200517235526_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122427",
                        "sortorder": 11,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074159/9AAD8E55FAD396A4A0B6B61A45E26B28687EF3EA/",
                        "size": 478634,
                        "filename": "20200517235542_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122428",
                        "sortorder": 12,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074181/475893AAFEBDC7C44CB40A651B3118D3C0D3C5DE/",
                        "size": 563097,
                        "filename": "20200517235624_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122429",
                        "sortorder": 13,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074191/4A721CFFA91B53BE05C40E1B80081C1408F46320/",
                        "size": 296901,
                        "filename": "20200517235700_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122430",
                        "sortorder": 14,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074202/2784BCB0C3F45AE0B487238EC466BB1CD1BD68BD/",
                        "size": 482422,
                        "filename": "20200517235705_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122431",
                        "sortorder": 15,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074210/0BB495AB795BF0755AE59EB8FE00E32887E839F3/",
                        "size": 325917,
                        "filename": "20200517235718_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122432",
                        "sortorder": 16,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074222/6A56BB158AA0303E865AAF47E42BE877F329E02A/",
                        "size": 441783,
                        "filename": "20200517235728_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122433",
                        "sortorder": 17,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074230/8B88EFDCEDD0DEF60EA36F15D78323C311D6AD10/",
                        "size": 477307,
                        "filename": "20200517235735_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122434",
                        "sortorder": 18,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074240/E0B1D14CD0C43F17FD7B2B6E7AF4BA87D2097A37/",
                        "size": 442290,
                        "filename": "20200517235755_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122435",
                        "sortorder": 19,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074251/741495F32F584CE23219B7CDF2EC10C7E3B36F58/",
                        "size": 511552,
                        "filename": "20200517235817_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122436",
                        "sortorder": 20,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074259/4DE7E9061D3BDDC6B7C5CA6995FD3D99B5A665DB/",
                        "size": 848443,
                        "filename": "20200517235828_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "19122437",
                        "sortorder": 21,
                        "url": "https://steamuserimages-a.akamaihd.net/ugc/1027329389695074267/4AC9DBF871C115DC270EF6D9D9A62D5276E4E067/",
                        "size": 344893,
                        "filename": "20200517235848_1.jpg",
                        "preview_type": 0,
                    },
                    {
                        "previewid": "21893051",
                        "sortorder": 22,
                        "youtubevideoid": "2xYzDODU6Ik",
                        "preview_type": 1,
                        "external_reference": "",
                    },
                ],
                "tags": [
                    {"tag": "Addon", "display_name": "Addon"},
                    {"tag": "map", "display_name": "map"},
                    {"tag": "Scenic", "display_name": "Scenic"},
                ],
                "vote_data": {
                    "score": 0.7626459002494812,
                    "votes_up": 146,
                    "votes_down": 11,
                },
                "playtime_stats": {"playtime_seconds": "0", "num_sessions": "0"},
                "language": 0,
                "maybe_inappropriate_sex": False,
                "maybe_inappropriate_violence": False,
                "revision_change_number": "33",
                "revision": 1,
                "ban_text_check_result": 0,
            }
        ]
    }
}
```

### Getting user wishlist data

This call does not require a Steam API Key

```python
import os
from steam_web_api import Steam

KEY = os.environ.get("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steam_id, page(0 default)
user = steam.users.get_profile_wishlist("<steam_id>")
```

#### Example response

```python
[
  {
    'appid': 3548580, 
    'priority': 0, 
    'date_added': 1749992867
  }, 
  {
    'appid': 3615290, 
    'priority': 0, 
    'date_added': 1746367747
  }
]
```
