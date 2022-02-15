import aiohttp
import json

from .exception import APIError, HistoryLimitError
from .objects.leaderboards import Leaderboards
from .objects.ranking import Ranking
from .objects.player import Player, Formatted
from .objects.api import Stats

class Observer:
    def __init__(self, key:str=""):
        self.key = key
        self.api = "https://api.invite.observer/v1"

    async def get_api_stats(self) -> Stats:
        try:
            async with aiohttp.request("GET", f"{self.api}/stats") as response:
                json = await response.json()
                if json['success']==True:
                    return Stats(json)
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
        
    async def get_lookback_stats(self, uuid, lookback) -> Player:
        if lookback>100:
            raise HistoryLimitError
        try:
            async with aiohttp.request("GET", f"{self.api}/lookback?uuid={uuid}&lookback={lookback}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "lookback")
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
            
    async def get_leaderboard_stats(self, type, gamemode, stat, start, end) -> Leaderboards:
        try:
            async with aiohttp.request("GET", f"{self.api}/leaderboards?type={type}&gamemode={gamemode}&stat={stat}&from={start}&to={end}") as response:
                json = await response.json()
                if json['success']==True:
                    return Leaderboards(json)
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_ranking_stats(self, uuid, type, gamemode, stat) -> Ranking:
        try:
            async with aiohttp.request("GET", f"{self.api}/ranking?uuid={uuid}&type={type}&gamemode={gamemode}&stat={stat}") as response:
                json = await response.json()
                if json['success']==True:
                    return Ranking(json)
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_daily_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/daily?uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "daily")
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_weekly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/weekly?uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "weekly")
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
            
    async def get_monthly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/monthly?uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "monthly")
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_formatted_stats(self, uuid) -> Formatted:
        try:
            async with aiohttp.request("GET", f"{self.api}/formatted?uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Formatted(json)
                else:
                    raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)