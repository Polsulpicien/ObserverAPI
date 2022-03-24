# Introduction

***From the official Observer API docs:***

This public API lets you access almost everything our backend keeps track of. Please note that any feature that uses this API can not be monetized.  

***

- [`Documentation`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#documentation)  
- [`Notes`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#notes)  
- [`Examples`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#examples)  

# Documentation

- [`ObserverAPI.Observer()`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/client.py#L2)
> Main function to start the Client.  
  This Function will also make your life easier, since you will only have to provide your API Key once!

***

## History: Everything related to historical stats
-  [`register`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#register) > Wrapper on the [Register](https://api.invite.observer/v1/register) endpoint of the Observer API
> Register a player for the leaderboards and historical stats tracking  
*The ratelimit for this endpoint is 25 registrations every ten minutes.*
-  [`daily`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#daily) > Wrapper on the [Daily](https://api.invite.observer/v1/daily) endpoint of the Observer API
> Get a player's stats from yesterday
-  [`weekly`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#weekly) > Wrapper on the [Weekly](https://api.invite.observer/v1/weekly) endpoint of the Observer API
> Get a player's stats from the beginning of the current week (Sunday)
-  [`monthly`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#monthly) > Wrapper on the [Monhtly](https://api.invite.observer/v1/monthly) endpoint of the Observer API
> Get a player's stats from the beginning of the current month (1st)
-  [`lookback`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#lookback) > Wrapper on the [Lookback](https://api.invite.observer/v1/lookback) endpoint of the Observer API
> Get a player's stats from a specific number of days ago
-  [`history`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#history) > Wrapper on the [History](https://api.invite.observer/v1/history) endpoint of the Observer API
> Get a player's stats between a specific number of days

***

## Leaderboards: Endpoints using leaderboard data
-  [`leaderboards`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#leaderboards) > Wrapper on the [Leaderboards](https://api.invite.observer/v1/leaderboards) endpoint of the Observer API
> Get the leaderboards for various timeframes, gamemodes and stat-types
-  [`ranking`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#ranking) > Wrapper on the [Ranking](https://api.invite.observer/v1/ranking) endpoint of the Observer API
> Get a player's ranking on a specific leaderboard  
*Ranking is not zero-based, so there's no need to add 1 to the result.*

***

## Misc
-  [`formatted`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#formatted) > Wrapper on the [Formatted](https://api.invite.observer/v1/formatted) endpoint of the Observer API
> Get a player's formatted name with Hypixel rank
-  [`stats`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#stats) > Wrapper on the [Stats](https://api.invite.observer/v1/stats) endpoint of the Observer API
> Get various statistics for the Observer bot
-  [`key`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#key) > Wrapper on the [Key](https://api.invite.observer/v1/api) endpoint of the Observer API
> Get statistics for your API key

Each class has a `data` argument so you can get the raw data if you want/need it.

## Observer

- `await Observer(key : str, message : bool = True, show_key : bool = False)`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `key` ([str](https://docs.python.org/3/library/functions.html#str)) > Observer API Key
    - `message` ([bool](https://docs.python.org/3/library/functions.html#bool)) > Display the API Key Stats
    - `show_key` ([bool](https://docs.python.org/3/library/functions.html#bool)) > Display the API Key

  - Raises:
    - [`InvalidAPIKeyError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L6) > Invalid API Key Error

## Register

- `await register.post(uuid : str) -> True`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `True` ([bool](https://docs.python.org/3/library/functions.html#bool)) > Returns True if the player is now Registered.

## Daily

- `await daily.get(uuid : str) -> Player`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) > A Player object
  
- `await daily.post(uuids : list) -> List`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> You provided more than 16 uuids!

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) object

## Weekly

- `await weekly.get(uuid : str) -> Player`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) > A Player object

- `await weekly.post(uuids : list) -> List`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> You provided more than 16 uuids!

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) object

## Monthly

- `await monthly.get(uuid : str) -> Player`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) > A Player object

- `await monthly.post(uuids : list) -> List`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> You provided more than 16 uuids!

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) object

## Lookback

- `await lookback.get(uuid : str, lookback : int = 1) -> Lookback`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `lookback` ([int](https://docs.python.org/3/library/functions.html#int)) > Numbers of days to lookback on a Player Stats

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> You provided more than 16 uuids!
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> Can not look back more than 100 days!

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) > A Player object
  
- `await lookback.post(uuids : list) -> List`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) object

## History

- `await history.get(uuid : str, start : int = 1, end : int = 10) -> Lookback`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `start` ([int](https://docs.python.org/3/library/functions.html#int)) > From
    - `end` ([int](https://docs.python.org/3/library/functions.html#int)) > to

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) > A Player object
  
- `await history.post(uuids : list, start : int = 1, end : int = 10) -> List`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)
    - `start` ([int](https://docs.python.org/3/library/functions.html#int)) > From
    - `end` ([int](https://docs.python.org/3/library/functions.html#int)) > to

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.
    - [`BadRequest`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L15)> You provided more than 16 uuids!

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md) object

***

## Leaderboards

- `await leaderboard.get(uuid : str, type : str, gamemode : str, stat : str) -> Leaderboards`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `type` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Type](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#type)
    - `gamemode` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Gamemode](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#gamemode)
    - `stat` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Stat](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#stat)
    - `start` ([int](https://docs.python.org/3/library/functions.html#int)) > Where to Start
    - `end` ([int](https://docs.python.org/3/library/functions.html#int)) > Where the Leaderboard should End

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `leaderboard` ([dict](https://docs.python.org/3/library/functions.html#dict)) > The Raw Leaderboard

- `get_index(index : int)`
  - Parameters:
      - `index` ([int](https://docs.python.org/3/library/functions.html#int)) > An Index

  - Return:
    - `rank` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player Rank
    - `id` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player ID
    - `value` ([int](https://docs.python.org/3/library/functions.html#int)) > The Value
    - `formatted` ([str](https://docs.python.org/3/library/functions.html#str)) > Formatted Player Name

## Ranking

- `await ranking.get(uuid : str, type : str, gamemode : str, stat : str) -> Ranking`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `type` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Type](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#type)
    - `gamemode` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Gamemode](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#gamemode)
    - `stat` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Stat](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#stat)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `rank` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player's Rank

- `await ranking.post(uuids : list, type : str, gamemode : str, stat : str) -> Ranking`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)
    - `type` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Type](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#type)
    - `gamemode` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Gamemode](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#gamemode)
    - `stat` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Stat](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#stat)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Ranking](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#ranking) object

***

## Formatted

- `await formatted.get(uuid : str) -> Formatted`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `formatted` ([str](https://docs.python.org/3/library/functions.html#str)) > The Formatted Username of the Player

- `await formatted.post(uuids : list) -> Formatted`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuids` ([list](https://docs.python.org/3/library/functions.html#list)) > A List of Players UUIDs (max 16)

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - [List](https://docs.python.org/3/library/functions.html#list) > A list of [Formatted](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#formatted) object

## Stats

- `await stats.get() -> Stats`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `tracked_players` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Player Tracked by the Observer API
    - `commands_executed` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Commands Executed via the Observer API
    - `verified_users` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Verified Users in the Observer API

## Key

- `await key.get() -> Key`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Raises:
    - [`APIError`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/exception.py#L1) > An error occured.

  - Return:
    - `key` ([str](https://docs.python.org/3/library/functions.html#str)) > The Observer API Key
    - `owner` ([str](https://docs.python.org/3/library/functions.html#str)) > The Observer API Key Discord ID
    - `limit` ([int](https://docs.python.org/3/library/functions.html#int)) > Key Requests Limit
    - `minute_queries` ([int](https://docs.python.org/3/library/functions.html#int)) > Last Minute Key Requests
    - `total_queries` ([int](https://docs.python.org/3/library/functions.html#int)) > Total Key Requests


# Notes

- All post endpoints, except the register endpoint, will return a list!  


- **For Daily, Weekly and Monthly stats, you'll need to compare them to the actual stats of the Player from the Hypixel API!**

# Examples

You can find all examples in the [`examples` folder](https://github.com/Polsulpicien/ObserverAPI/tree/main/examples)

- [`Basic`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/tree/main/examples/main.py)
- [`Register`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/tree/main/examples/register.py)
- [`Daily / Weekly / Monthly`](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/tree/main/examples/daily.py)

*I haven't made examples on all endpoints, tell me if you want some ;)*
