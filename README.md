# Get Started

## Installation

`pip install python-steam-api`

## Pip install requirements

`pip install beautifulsoup4`

## Create Steam API web key

[Steam API Web key](https://steamcommunity.com/dev/apikey)

Follow instructions to get API Key

## Create .env file

From root of your project

`touch .env`

`echo "STEAM_API_KEY=<YOUR_STEAM_API KEY>" >> .env`

# Basic Usage

### Searching for a user

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam()

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
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam()

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
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

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

### Getting Users Recently Played Games

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid
user = steam.users.get_user_recently_played_games("76561198995017863")
```

### Getting User Owned Games

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid
user = steam.users.get_owned_games("76561198995017863")
```

### Getting User Steam Level

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid
user = steam.users.get_user_steam_level("76561198995017863")
```

### Getting User Badges

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid
user = steam.users.get_user_badges("76561198995017863")
```

### Getting Community Badge Progress

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid, badgeid
user = steam.users.get_community_badge_progress("<steam_id>", "<badge_id>")
```

### Getting User Public Account

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steamid
user = steam.users.get_account_public_info("<steam_id>")
```

### Searching for Games

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

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

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


terraria_app_id = 105600
steam = Steam()

# arguments: app_id
user = steam.apps.get_app_details(terraria_app_id)
```

Response

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
      "header_image": "https://cdn.akamai.steamstatic.com/steam/apps/105600/header.jpg?t=1590092560",
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
      },
      "developers": ["Re-Logic"],
      "publishers": ["Re-Logic"],
      "price_overview": {
        "currency": "KRW",
        "initial": 1050000,
        "final": 1050000,
        "discount_percent": 0,
        "initial_formatted": "",
        "final_formatted": "₩ 10,500"
      },
      "packages": [8183, 356628, 8184],
      "package_groups": [
        {
          "name": "default",
          "title": "Buy Terraria",
          "description": "",
          "selection_text": "Select a purchase option",
          "save_text": "",
          "display_type": 0,
          "is_recurring_subscription": "false",
          "subs": [
            {
              "packageid": 8183,
              "percent_savings_text": " ",
              "percent_savings": 0,
              "option_text": "Terraria - ₩ 10,500",
              "option_description": "",
              "can_get_free_license": "0",
              "is_free_license": false,
              "price_in_cents_with_discount": 1050000
            },
            {
              "packageid": 356628,
              "percent_savings_text": " ",
              "percent_savings": 0,
              "option_text": "Terraria - Commercial License - ₩ 10,500",
              "option_description": "",
              "can_get_free_license": "0",
              "is_free_license": false,
              "price_in_cents_with_discount": 1050000
            },
            {
              "packageid": 8184,
              "percent_savings_text": " ",
              "percent_savings": 0,
              "option_text": "Terraria 4-Pack - ₩ 32,000",
              "option_description": "",
              "can_get_free_license": "0",
              "is_free_license": false,
              "price_in_cents_with_discount": 3200000
            }
          ]
        }
      ],
      "platforms": {
        "windows": true,
        "mac": true,
        "linux": true
      },
      "metacritic": {
        "score": 83,
        "url": "https://www.metacritic.com/game/pc/terraria?ftag=MCD-06-10aaa1f"
      },
      "categories": [
        {
          "id": 2,
          "description": "Single-player"
        },
        {
          "id": 1,
          "description": "Multi-player"
        },
        {
          "id": 49,
          "description": "PvP"
        },
        {
          "id": 36,
          "description": "Online PvP"
        },
        {
          "id": 9,
          "description": "Co-op"
        },
        {
          "id": 38,
          "description": "Online Co-op"
        },
        {
          "id": 22,
          "description": "Steam Achievements"
        },
        {
          "id": 28,
          "description": "Full controller support"
        },
        {
          "id": 29,
          "description": "Steam Trading Cards"
        },
        {
          "id": 23,
          "description": "Steam Cloud"
        },
        {
          "id": 41,
          "description": "Remote Play on Phone"
        },
        {
          "id": 42,
          "description": "Remote Play on Tablet"
        },
        {
          "id": 43,
          "description": "Remote Play on TV"
        }
      ],
      "genres": [
        {
          "id": "1",
          "description": "Action"
        },
        {
          "id": "25",
          "description": "Adventure"
        },
        {
          "id": "23",
          "description": "Indie"
        },
        {
          "id": "3",
          "description": "RPG"
        }
      ],
      "screenshots": [
        {
          "id": 0,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_8c03886f214d2108cafca13845533eaa3d87d83f.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_8c03886f214d2108cafca13845533eaa3d87d83f.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 1,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_ae168a00ab08104ba266dc30232654d4b3c919e5.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_ae168a00ab08104ba266dc30232654d4b3c919e5.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 2,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_9edd98caaf9357c2f40758f354475a56e356e8b0.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_9edd98caaf9357c2f40758f354475a56e356e8b0.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 3,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_75ea9a7e39eb34b40efa1e6dfd2536098dc4734b.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_75ea9a7e39eb34b40efa1e6dfd2536098dc4734b.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 4,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_782374517c1792debd74d24856203b876eba3a5d.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_782374517c1792debd74d24856203b876eba3a5d.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 5,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_04dd9f0a5773b686a452ba480b951f83b3ed5061.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_04dd9f0a5773b686a452ba480b951f83b3ed5061.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 6,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_26c4a091c482be28efe1ecf4dfb498273e5a9107.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_26c4a091c482be28efe1ecf4dfb498273e5a9107.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 7,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_830aa37570410b80947636785ff62096c0bf276f.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_830aa37570410b80947636785ff62096c0bf276f.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 8,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_0d805c81ef85dfd2a7a8b25da96f8066017fb3b3.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_0d805c81ef85dfd2a7a8b25da96f8066017fb3b3.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 9,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_b28125b8b8ccacbbb38a3ab4ceaf406ec94d98a4.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_b28125b8b8ccacbbb38a3ab4ceaf406ec94d98a4.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 10,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_900453507c3eb3df55175fb1362869cc75203594.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_900453507c3eb3df55175fb1362869cc75203594.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 11,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a1dbbda90ea1669da35cf277e65b5191565bcb12.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a1dbbda90ea1669da35cf277e65b5191565bcb12.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 12,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a34d1ebdc99634e012ea19759c12822802164b0e.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a34d1ebdc99634e012ea19759c12822802164b0e.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 13,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_6f57075d0d8f9d2fd963b74f9a4526bbf91aab10.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_6f57075d0d8f9d2fd963b74f9a4526bbf91aab10.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 14,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_ab3143003094dec454c5a76cc7d7948f17ca7517.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_ab3143003094dec454c5a76cc7d7948f17ca7517.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 15,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_1a091473c0b53e98d7a0708dd3ec0978dd56ba45.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_1a091473c0b53e98d7a0708dd3ec0978dd56ba45.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 16,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a81bfb762197b0aafc207274a708d79e7c39e45f.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_a81bfb762197b0aafc207274a708d79e7c39e45f.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 17,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_fefd40cad50a10c09f928f9dc3f9017f8fe50213.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_fefd40cad50a10c09f928f9dc3f9017f8fe50213.1920x1080.jpg?t=1590092560"
        },
        {
          "id": 18,
          "path_thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_fd3a47380882311f6ff80cb2d4491d1de4af9e8b.600x338.jpg?t=1590092560",
          "path_full": "https://cdn.akamai.steamstatic.com/steam/apps/105600/ss_fd3a47380882311f6ff80cb2d4491d1de4af9e8b.1920x1080.jpg?t=1590092560"
        }
      ],
      "movies": [
        {
          "id": 256785003,
          "name": "Terraria: Journey's End Trailer",
          "thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/256785003/movie.293x165.jpg?t=1589654781",
          "webm": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/256785003/movie480_vp9.webm?t=1589654781",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/256785003/movie_max_vp9.webm?t=1589654781"
          },
          "mp4": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/256785003/movie480.mp4?t=1589654781",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/256785003/movie_max.mp4?t=1589654781"
          },
          "highlight": true
        },
        {
          "id": 2040428,
          "name": "Terraria 1.3 Trailer",
          "thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/2040428/movie.293x165.jpg?t=1447376855",
          "webm": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/2040428/movie480.webm?t=1447376855",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/2040428/movie_max.webm?t=1447376855"
          },
          "mp4": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/2040428/movie480.mp4?t=1447376855",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/2040428/movie_max.mp4?t=1447376855"
          },
          "highlight": true
        },
        {
          "id": 2029566,
          "name": "Terraria 1.2 Trailer",
          "thumbnail": "https://cdn.akamai.steamstatic.com/steam/apps/2029566/movie.293x165.jpg?t=1447358964",
          "webm": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/2029566/movie480.webm?t=1447358964",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/2029566/movie_max.webm?t=1447358964"
          },
          "mp4": {
            "480": "http://cdn.akamai.steamstatic.com/steam/apps/2029566/movie480.mp4?t=1447358964",
            "max": "http://cdn.akamai.steamstatic.com/steam/apps/2029566/movie_max.mp4?t=1447358964"
          },
          "highlight": true
        }
      ],
      "recommendations": {
        "total": 787917
      },
      "achievements": {
        "total": 104,
        "highlighted": [
          {
            "name": "Timber!!",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/0fbb33098c9da39d1d4771d8209afface9c46e81.jpg"
          },
          {
            "name": "No Hobo",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/65bbc5ea6a030b963d9a06e5e1b315c3872837a3.jpg"
          },
          {
            "name": "Stop! Hammer Time!",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/4760436e9973519098bb2cc419339d24e56af139.jpg"
          },
          {
            "name": "Ooo! Shiny!",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/57b929ffd1a732ffc49abc6c53387e08bac4cbbb.jpg"
          },
          {
            "name": "Heart Breaker",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/8243e4a0f7f803cd06cf37d64d11e04697afe30c.jpg"
          },
          {
            "name": "Heavy Metal",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/f727271437793b278c809a067fa2334ea2846f34.jpg"
          },
          {
            "name": "I Am Loot!",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/6705287adc42e2741d632c2d714424b2aa3e5716.jpg"
          },
          {
            "name": "Star Power",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/738ca7765e32895918979d31d600d19254b14190.jpg"
          },
          {
            "name": "Hold on Tight!",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/0e2a5e080563ce9c30cf3b45dd155d18640f0bf6.jpg"
          },
          {
            "name": "Eye on You",
            "path": "https://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/105600/b10b068163125e13444e2cdb145c1a200c7ad607.jpg"
          }
        ]
      },
      "release_date": {
        "coming_soon": false,
        "date": "16 May, 2011"
      },
      "support_info": {
        "url": "https://forums.terraria.org/index.php?forums/pc-support.102/",
        "email": "support@terraria.org"
      },
      "background": "https://cdn.akamai.steamstatic.com/steam/apps/105600/page_bg_generated_v6b.jpg?t=1590092560",
      "background_raw": "https://cdn.akamai.steamstatic.com/steam/apps/105600/page.bg.jpg?t=1590092560",
      "content_descriptors": {
        "ids": [],
        "notes": null
      }
    }
  }
}
```

### Getting user app stats

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steam_id, app_id
user = steam.apps.get_user_stats("<steam_id>", "<app_id>")
```

### Getting user app achievements

```python
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam()

# arguments: steam_id, app_id
user = steam.apps.get_user_achievements("<steam_id>", "<app_id>")
```
