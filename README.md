# Get Started

## Create Python Virtual Enviornment

1. `python -m venv venv` or `python3 -m venv venv`

If on Windows

2. `source venv/Scripts/active`

If on Linux or Mac

2. `. venv/bin/activate`

## Pip install requirements

`pip install -r requirements.txt`

## Create Steam API web key

[Steam API Web key](https://steamcommunity.com/dev/apikey)

Follow instructions to get API Key

## Create .env file

From root

`touch .env`

`echo "STEAM_API_KEY=<'Your Steam API KEY'>" >> .env`

# Basic Usage

### Searching for a user

```python
steam = Steam(API_KEY)

user = steam.users.search_user("the12thchairman")
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
steam = Steam(API_KEY)

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
steam = Steam(API_KEY)

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
      "steamid": "76561198121423211",
      "communityvisibilitystate": 3,
      "profilestate": 1,
      "personaname": "el_nave",
      "profileurl": "https://steamcommunity.com/profiles/76561198121423211/",
      "avatar": "https://avatars.akamai.steamstatic.com/1f48ca0206ad63f430b35173c0c994d26e8fed91.jpg",
      "avatarmedium": "https://avatars.akamai.steamstatic.com/1f48ca0206ad63f430b35173c0c994d26e8fed91_medium.jpg",
      "avatarfull": "https://avatars.akamai.steamstatic.com/1f48ca0206ad63f430b35173c0c994d26e8fed91_full.jpg",
      "avatarhash": "1f48ca0206ad63f430b35173c0c994d26e8fed91",
      "lastlogoff": 1659839839,
      "personastate": 3,
      "primaryclanid": "103582791429521408",
      "timecreated": 1388690569,
      "personastateflags": 0,
      "relationship": "friend",
      "friend_since": 1592096466
    },
    {
      "steamid": "76561198062000703",
      "communityvisibilitystate": 3,
      "profilestate": 1,
      "personaname": "Term",
      "profileurl": "https://steamcommunity.com/id/_terminus14/",
      "avatar": "https://avatars.akamai.steamstatic.com/eab71f1cb5d312c9b801e04a8da8b81d246bf6af.jpg",
      "avatarmedium": "https://avatars.akamai.steamstatic.com/eab71f1cb5d312c9b801e04a8da8b81d246bf6af_medium.jpg",
      "avatarfull": "https://avatars.akamai.steamstatic.com/eab71f1cb5d312c9b801e04a8da8b81d246bf6af_full.jpg",
      "avatarhash": "eab71f1cb5d312c9b801e04a8da8b81d246bf6af",
      "lastlogoff": 1659632671,
      "personastate": 0,
      "primaryclanid": "103582791434476706",
      "timecreated": 1334459945,
      "personastateflags": 0,
      "relationship": "friend",
      "friend_since": 1648350663
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

# MORE DOCUMENTATION TO COME
