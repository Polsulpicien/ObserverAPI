import json

from . import requests

async def Observer(key:str, message=True, show_key=False):
    """
    Function to start the Main Client.
    This can error with either InvalidAPIKeyError if the Key is invalid or APIError if the API can't be reach.
    This Function will also make your life easier, since you will only have to provide your API Key once!

    > Parameters:
      - key, type(str), required > Observer API Key
      - message, type(bool), True by default > Display the API Key Stats
      - show_key, type(bool), False by default > Display the API Key

    > Return:
      - ObserverClient, type(class) > Main Client
    """
    client = ObserverClient(key)
    key = await client.api.get()
    if message==True:
        if show_key==True:
            print(f"\nObserverAPI >>https://github.com/Polsulpicien/ObserverAPI<<\n\nClient started successfully:\n- Owner: {key.owner} [https://lookup.guru/{key.owner}]\n- Key: {key.key}\n- Limit: {key.limit}\n- Total Queries: {key.total_queries}\n")
        else:
            print(f"\nObserverAPI >>https://github.com/Polsulpicien/ObserverAPI<<\n\nClient started successfully:\n- Owner: {key.owner} [https://lookup.guru/{key.owner}]\n- Key: \n- Limit: {key.limit}\n- Total Queries: {key.total_queries}\n")
    return client
        
class ObserverClient:
    """
    Main client object of ObserverAPI library. This saves the API key provided and creates separate objects for each Observer API methods
    """
    def __init__(self, key:str):
        self.key=key
        self.api = Api(self.key)
        self.stats = Stats(self.key)
        self.lookback = Lookback(self.key)
        self.leaderboard = Leaderboards(self.key)
        self.ranking = Ranking(self.key)
        self.daily = Daily(self.key)
        self.weekly = Weekly(self.key)
        self.monthly = Monthly(self.key)
        self.formatted = Formatted(self.key)

class Api():
    """
    Wrapper on the /key endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self):
        """
        Queries the API

        > Return:
          - Key, type(class) > API Key Stats
        """
        return await requests.Observer(self.key).get_api_stats()
        
class Stats():
    """
    Wrapper on the /stats endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self):
        """
        Queries the API

        > Return:
          - Stats, type(class) > API Stats
        """
        return await requests.Observer(self.key).get_observer_api_stats()

class Lookback():
    """
    Wrapper on the /lookback endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str, lookback:int=1):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID
          - lookback, type(int) > Number of Days to Lookback (max 100 at the moment, this can error with HistoryLimitError if you try go fetch more!)

        > Return:
          - Lookback, type(class) > Lookback Stats or a player
        """
        return await requests.Observer(self.key).get_lookback_stats(uuid, lookback)

class Leaderboards():
    """
    Wrapper on the /leaderboards endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, type:str, gamemode:str, stat:str, start:int, end:int):
        """
        Queries the API

        > Parameters:
          - type, type(str) > Timeframe of the leaderboard 
          - gamemode, type(str) > The gamemode of the leaderboard
          - stats, type(str) > The stat-type of the leaderboard
          - start, type(int) > Where to Start
          - end, type(int) > Where the Leaderboard should End

        > Return:
          - Leaderboards, type(class) > A Leaderboard
        """
        return await requests.Observer(self.key).get_leaderboard_stats(type, gamemode, stat, start, end)

class Ranking():
    """
    Wrapper on the /ranking endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str, type:str, gamemode:str, stat:str):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID
          - type, type(str) > Timeframe of the leaderboard 
          - gamemode, type(str) > The gamemode of the leaderboard
          - stats, type(str) > The stat-type of the leaderboard

        > Return:
          - Ranking, type(class) > Ranking Stats
        """
        return await requests.Observer(self.key).get_ranking_stats(uuid, type, gamemode, stat)
        
class Daily():
    """
    Wrapper on the /daily endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID

        > Return:
          - Daily, type(class) > Daily Stats of a Player
        """
        return await requests.Observer(self.key).get_daily_stats(uuid)

class Weekly():
    """
    Wrapper on the /weekly endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID

        > Return:
          - Weekly, type(class) > Weekly Stats of a Player
        """
        return await requests.Observer(self.key).get_weekly_stats(uuid)
        
class Monthly():
    """
    Wrapper on the /monthly endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID

        > Return:
          - Monthly, type(class) > Monthly Stats of a Player
        """
        return await requests.Observer(self.key).get_monthly_stats(uuid)

class Formatted():
    """
    Wrapper on the /formatted endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        """
        Queries the API

        > Parameters:
          - uuid, type(str) > A Player UUID

        > Return:
          - Formatted, type(class) > Formatted Username of a Player
        """
        return await requests.Observer(self.key).get_formatted_stats(uuid)