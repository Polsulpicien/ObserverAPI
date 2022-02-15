# Documentation

[`ObserverAPI.Observer()`:](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/client.py#L5)

**Observer Client, this will be useful when they will add the api key.**

-  [`stats`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#stats) > Wrapper on the [Stats](https://api.invite.observer/v1/stats) endpoint of the Observer API
> Returns the count of tracked players, total number of commands executed and verified players for Observer  
-  [`lookback`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#lookback) > Wrapper on the [Lookback](https://api.invite.observer/v1/lookback) endpoint of the Observer API
> Get the stats for a player from X days ago  
-  [`ranking`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#ranking) > Wrapper on the [Ranking](https://api.invite.observer/v1/ranking) endpoint of the Observer API
> Get the ranking for a player on a specific leaderboard  
-  `daily` > Wrapper on the [Daily](https://api.invite.observer/v1/daily) endpoint of the Observer API
> Get the stats of a player from yesterday  
-  `weekly` > Wrapper on the [Weekly](https://api.invite.observer/v1/weekly) endpoint of the Observer API
> Get the stats of a player from the beginning of the week (Sunday)  
-  `monthly` > Wrapper on the [Monhtly](https://api.invite.observer/v1/monthly) endpoint of the Observer API
> Get the stats of a player from the first day of the month  
-  `formatted` > Wrapper on the [Formatted](https://api.invite.observer/v1/formatted) endpoint of the Observer API
> Get the formatted name of a player if they're registered on Observer  

Each class has a `data` argument so you can get the raw data if you want/need it.

## Stats

- `await stats.get() -> Stats`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - None

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

## Ranking

- `await ranking.get(uuid : str, type : str, gamemode : str, stat : str) -> Lookback`  
  *This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).*

  - Parameters:
    - `uuid` ([str](https://docs.python.org/3/library/functions.html#str)) > A Player UUID
    - `type` ([str](https://docs.python.org/3/library/functions.html#int)) > A [Observer API Type]()

  - Raises:
    - APIError > An error occured.

  - Return:
    - [Player Class](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/player.md)

  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)
