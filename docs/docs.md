# Documentation

[`ObserverAPI.Observer()`:](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/client.py#L5)

**Observer Client, this will be useful when they will add the api key.**

-  [`stats`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#stats) > Wrapper on the [Stats](https://api.invite.observer/v1/stats) endpoint of the Observer API
> Returns the count of tracked players, total number of commands executed and verified players for Observer  
-  [`lookback`](https://github.com/Polsulpicien/ObserverAPI/blob/main/docs/docs.md#lookback) > Wrapper on the [Lookback](https://api.invite.observer/v1/lookback) endpoint of the Observer API
> Get the stats for a player from X days ago  
-  `ranking` > Wrapper on the [Ranking](https://api.invite.observer/v1/ranking) endpoint of the Observer API
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
    - `timestamp` ([int](https://docs.python.org/3/library/functions.html#int)) > ?
    - `wins` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Wins
    - `coins` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Coins
    - `karma` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Karma
    - `achievementPoints` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Achievement Points
    - `experience` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Experience
    - `quests` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Quests
    - `challenges` ([int](https://docs.python.org/3/library/functions.html#int)) > Number of Challenges
    - `reset` ([int](https://docs.python.org/3/library/functions.html#int)) > Time of the last reset

    - `arenabrawl` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `bedwars` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `blitz` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `buildbattle` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `copsandcrims` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `duels` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `megawalls` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `murdermystery` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `paintball` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `quakecraft` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `skywars` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `smashheroes` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `speeduhc` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `tntgames` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `turbokart` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `uhc` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `vampirez` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `walls` ([int](https://docs.python.org/3/library/functions.html#int)) >
    - `warlords` ([int](https://docs.python.org/3/library/functions.html#int)) >


  - Return Type:
    - [Player](https://github.com/Polsulpicien/ObserverAPI/blob/main/ObserverAPI/objects/player.py#L5)
