from . import requests

async def Observer(key:str, message=True, show_key=False):
    client = ObserverClient(key)
    key = await client.key.get()
    if message==True:
        if show_key==True:
            print(f"\nObserverAPI >>https://github.com/Polsulpicien/ObserverAPI<<\n\nClient started successfully:\n- Owner: {key.owner} [https://lookup.guru/{key.owner}]\n- Key: {key.key}\n- Limit: {key.limit}\n- Minute Queries: {key.minute_queries}\n- Total Queries: {key.total_queries}\n")
        else:
            print(f"\nObserverAPI >>https://github.com/Polsulpicien/ObserverAPI<<\n\nClient started successfully:\n- Owner: {key.owner} [https://lookup.guru/{key.owner}]\n- Key: \n- Limit: {key.limit}\n- Minute Queries: {key.minute_queries}\n- Total Queries: {key.total_queries}\n")
    return client
        
class ObserverClient:
    """
    Main client object of ObserverAPI library. This saves the API key provided and creates separate objects for each Observer API methods
    """
    def __init__(self, api:str):
        self.register = Register(api)
        self.daily = Daily(api)
        self.weekly = Weekly(api)
        self.monthly = Monthly(api)
        self.lookback = Lookback(api)
        self.history = History(api)
        
        self.leaderboard = Leaderboards(api)
        self.ranking = Ranking(api)

        self.formatted = Formatted(api)
        self.stats = Stats(api)
        self.key = Key(api)
        
###########################
#                         #
#         History         #
#                         #
###########################

class Register():
    """
    Wrapper on the /register post endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def post(self, uuid:str):
        return await requests.Observer(self.key).post_register(uuid)

class Daily():
    """
    Wrapper on the /daily endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        return await requests.Observer(self.key).get_daily_stats(uuid)

    async def post(self, uuids:list):
        return await requests.Observer(self.key).post_daily_stats(uuids)

class Weekly():
    """
    Wrapper on the /weekly endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        return await requests.Observer(self.key).get_weekly_stats(uuid)

    async def post(self, uuids:list):
        return await requests.Observer(self.key).post_weekly_stats(uuids)
        
class Monthly():
    """
    Wrapper on the /monthly endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        return await requests.Observer(self.key).get_monthly_stats(uuid)

    async def post(self, uuids:list):
        return await requests.Observer(self.key).post_monthly_stats(uuids)

class Lookback():
    """
    Wrapper on the /lookback endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str, lookback:int=1):
        return await requests.Observer(self.key).get_lookback_stats(uuid, lookback)

    async def post(self, uuids:list, lookback:int=1):
        return await requests.Observer(self.key).post_lookback_stats(uuids, lookback)

class History():
    """
    Wrapper on the /history endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str, start:int=1, end:int=10):
        return await requests.Observer(self.key).get_history_stats(uuid, start, end)

    async def post(self, uuids:list, start:int=1, end:int=10):
        return await requests.Observer(self.key).post_history_stats(uuids, start, end)

###########################
#                         #
#      Leaderboards       #
#                         #
###########################

class Leaderboards():
    """
    Wrapper on the /leaderboards endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, type:str, gamemode:str, stat:str, start:int, end:int):
        return await requests.Observer(self.key).get_leaderboard_stats(type, gamemode, stat, start, end)

class Ranking():
    """
    Wrapper on the /ranking endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str, type:str, gamemode:str, stat:str):
        return await requests.Observer(self.key).get_ranking_stats(uuid, type, gamemode, stat)

    async def post(self, uuids:list, type:str, gamemode:str, stat:str):
        return await requests.Observer(self.key).post_ranking_stats(uuids, type, gamemode, stat)
        
###########################
#                         #
#          Misc           #
#                         #
###########################

class Formatted():
    """
    Wrapper on the /formatted endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self, uuid:str):
        return await requests.Observer(self.key).get_formatted_stats(uuid)
    
    async def post(self, uuids:list):
        return await requests.Observer(self.key).post_formatted_stats(uuids)

class Stats():
    """
    Wrapper on the /stats endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self):
        return await requests.Observer(self.key).get_api_stats()

class Key():
    """
    Wrapper on the /key endpoint
    """
    def __init__(self, key:str):
        self.key = key

    async def get(self):
        return await requests.Observer(self.key).get_key_stats()