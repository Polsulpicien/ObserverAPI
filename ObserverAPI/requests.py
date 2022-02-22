import aiohttp
import json

from .exception import APIError, HistoryLimitError, InvalidAPIKeyError
from .objects.leaderboards import Leaderboards
from .objects.ranking import Ranking
from .objects.player import Player, Formatted
from .objects.api import Stats, Key

class Observer:
    def __init__(self, key:str):
        self.key = key
        self.api = "https://api.invite.observer/v1"

    async def get_api_stats(self) -> Key:
        try:
            async with aiohttp.request("GET", f"{self.api}/key?key={self.key}") as response:
                json = await response.json()
                if json['success']==True:
                    return Key(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
            
    async def get_observer_api_stats(self) -> Stats:
        try:
            async with aiohttp.request("GET", f"{self.api}/stats?key={self.key}") as response:
                json = await response.json()
                if json['success']==True:
                    return Stats(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
        
    async def get_lookback_stats(self, uuid, lookback) -> Player:
        if lookback>100:
            raise HistoryLimitError
        try:
            async with aiohttp.request("GET", f"{self.api}/lookback?key={self.key}&uuid={uuid}&lookback={lookback}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "lookback")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
            
    async def get_leaderboard_stats(self, type, gamemode, stat, start, end) -> Leaderboards:
        try:
            async with aiohttp.request("GET", f"{self.api}/leaderboards?key={self.key}&type={type}&gamemode={gamemode}&stat={stat}&from={start}&to={end}") as response:
                json = await response.json()
                if json['success']==True:
                    return Leaderboards(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_ranking_stats(self, uuid, type, gamemode, stat) -> Ranking:
        try:
            async with aiohttp.request("GET", f"{self.api}/ranking?key={self.key}&uuid={uuid}&type={type}&gamemode={gamemode}&stat={stat}") as response:
                json = await response.json()
                if json['success']==True:
                    return Ranking(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_daily_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/daily?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "daily")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_weekly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/weekly?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "weekly")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)
            
    async def get_monthly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/monthly?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "monthly")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)

    async def get_formatted_stats(self, uuid) -> Formatted:
        try:
            async with aiohttp.request("GET", f"{self.api}/formatted?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Formatted(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except Exception as error:
            raise APIError(error, 0)