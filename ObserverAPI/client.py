import json

from . import observer

async def Observer():
    """This will be easy to update and will not break everything when they will update the API to API Key only! ;)"""
    return ObserverClient()
        
class ObserverClient:
    def __init__(self):
        self.stats = Stats()
        self.lookback = Lookback()
        self.leaderboard = Leaderboards()
        self.ranking = Ranking()
        self.daily = Daily()
        self.weekly = Weekly()
        self.monthly = Monthly()
        self.formatted = Formatted()

class Stats():
    async def get(self):
        return await observer.Observer().get_api_stats()

class Lookback():
    async def get(self, uuid:str, lookback:int=1):
        return await observer.Observer().get_lookback_stats(uuid, lookback)

class Leaderboards():
    async def get(self, type:str, gamemode:str, stat:str, start:int, end:int):
        return await observer.Observer().get_leaderboard_stats(type, gamemode, stat, start, end)

class Ranking():
    async def get(self, uuid:str, type:str, gamemode:str, stat:str):
        return await observer.Observer().get_ranking_stats(uuid, type, gamemode, stat)

class Daily():
    async def get(self, uuid:str):
        return await observer.Observer().get_daily_stats(uuid)

class Weekly():
    async def get(self, uuid:str):
        return await observer.Observer().get_weekly_stats(uuid)
        
class Monthly():
    async def get(self, uuid:str):
        return await observer.Observer().get_monthly_stats(uuid)

class Formatted():
    async def get(self, uuid:str):
        return await observer.Observer().get_formatted_stats(uuid)