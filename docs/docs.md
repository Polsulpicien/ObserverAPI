# Documentation

[`ObserverAPI.Observer()`:](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/client.py#L5)

**Observer Client, this will be useful when they will add the api key.**

-  [`stats`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#stats) > Wrapper on the [Stats](https://api.invite.observer/v1/stats) endpoint of the Observer API
> Returns the count of tracked players, total number of commands executed and verified players for Observer  
-  [`lookback`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#lookback) > Wrapper on the [Lookback](https://api.invite.observer/v1/lookback) endpoint of the Observer API
> Get the stats for a player from X days ago  
-  [`leaderboards`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#leaderboards) > Wrapper on the [Leaderboards](https://api.invite.observer/v1/leaderboards) endpoint of the Observer API
> Get the leaderboards for a specific timeframe, gamemode and stat-type
-  [`ranking`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#ranking) > Wrapper on the [Ranking](https://api.invite.observer/v1/ranking) endpoint of the Observer API
> Get the ranking for a player on a specific leaderboard  
-  [`daily`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#rankdailying) > Wrapper on the [Daily](https://api.invite.observer/v1/daily) endpoint of the Observer API
> Get the stats of a player from yesterday  
-  [`weekly`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#weekly) > Wrapper on the [Weekly](https://api.invite.observer/v1/weekly) endpoint of the Observer API
> Get the stats of a player from the beginning of the week (Sunday)  
-  [`monthly`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#monthly) > Wrapper on the [Monhtly](https://api.invite.observer/v1/monthly) endpoint of the Observer API
> Get the stats of a player from the first day of the month  
-  [`formatted`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#formatted) > Wrapper on the [Formatted](https://api.invite.observer/v1/formatted) endpoint of the Observer API
> Get the formatted name of a player if they're registered on Observer  

Each class has a `data` argument so you can get the raw data if you want/need it.

## Stats

- `await stats.get() -> Stats`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Raises:
    - APIError > An error occured.

  - Return:
    - `trackedPlayers` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Player Tracked by the Observer API
    - `commandsExecuted` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Commands Executed via the Observer API
    - `verifiedUsers` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Verified Users in the Observer API

  - Return Type:
    - [Stats](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/api.py#L1)

## Lookback

- `await lookback.get(uuid : str, lookback : int = 1) -> Lookback`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `lookback` ([int](https://docs.python.org/3/library/functions.html#int)) > Numbers of days to lookback on a Player Stats

  - Raises:
    - APIError > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md)

  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)

## Leaderboards

- `await ranking.get(uuid : str, type : str, gamemode : str, stat : str) -> Ranking`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `type` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Type](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#type)
    - `gamemode` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Gamemode](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#gamemode)
    - `stat` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Stat](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#stat)
    - `start` ([int](https://docs.python.org/3/library/functions.html#int)) > Where to Start
    - `end` ([int](https://docs.python.org/3/library/functions.html#int)) > Where the Leaderboard should End

  - Raises:
    - APIError > An error occured.

  - Return:
    - `rank` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player Rank

  - Return Type:
    - [Ranking](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/ranking.py#L1)

- `get_index(index : int)`
  - Parameters:
      - `index` ([int](https://docs.python.org/3/library/functions.html#int)) > An Index

    - Raises:
      - HistoryLimitError > Can not look back more than 100 days!

    - Return:
      - `rank` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player Rank
      - `id` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player ID
      - `value` ([int](https://docs.python.org/3/library/functions.html#int)) > The Value
      - `formatted` ([str](https://docs.python.org/3/library/functions.html#str)) > Formatted Player Name

    - Return Type:
      - [Leaderboars](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/leaderboar.py#L1)


## Ranking

- `await ranking.get(uuid : str, type : str, gamemode : str, stat : str) -> Ranking`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `type` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Type](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#type)
    - `gamemode` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Gamemode](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#gamemode)
    - `stat` ([str](https://docs.python.org/3/library/functions.html#str)) > A [Observer API Stat](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/parameters.md#stat)

  - Raises:
    - APIError > An error occured.

  - Return:
    - `rank` ([int](https://docs.python.org/3/library/functions.html#int)) > The Player Rank

  - Return Type:
    - [Ranking](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/ranking.py#L1)

## Daily

- `await daily.get(uuid : str) -> Daily`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

- Raises:
    - APIError > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md)

  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)

## Weekly

- `await weekly.get(uuid : str) -> Weekly`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

- Raises:
    - APIError > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md)

  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)

## Monthly

- `await daily.get(uuid : str) -> Monthly`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

- Raises:
    - APIError > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md)

  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)

## Formatted

- `await daily.get(uuid : str) -> Formatted`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID

- Raises:
    - APIError > An error occured.

  - Return:
    - `formatted` ([str](https://docs.python.org/3/library/functions.html#str)) > The Formatted Name of the Player

  - Return Type:
    - [Formatted](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L1)

## Examples

You can find Examples in the [`tests` folder](https://github.com/Polsulpicien/ObserverAPI/tree/main/tests)
