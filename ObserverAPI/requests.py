import aiohttp

from .exception import InvalidAPIKeyError, APIError, NotRegistered, BadRequest
from .objects.leaderboards import Leaderboards
from .objects.ranking import Ranking
from .objects.player import Player, Formatted
from .objects.api import Stats, Key
from .utils import DEFAULT

class Observer:
    def __init__(self, key:str):
        self.key = key
        self.api = "https://api.invite.observer/v1"


    ###########################
    #                         #
    #         History         #
    #                         #
    ###########################

    async def post_register(self, uuid):
        try:
            async with aiohttp.request("POST", f"{self.api}/register?key={self.key}", data={'uuid': f'{uuid}'}) as response:
                json = await response.json()
                if json['success']==True:
                    return True
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def get_daily_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/daily?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "daily")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def post_daily_stats(self, uuids):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/daily?key={self.key}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Player(json['daily'][i]))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def get_weekly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/weekly?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "weekly")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def post_weekly_stats(self, uuids):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/weekly?key={self.key}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Player(json['weekly'][i]))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def get_monthly_stats(self, uuid) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/monthly?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "monthly")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def post_monthly_stats(self, uuids):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/monthly?key={self.key}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Player(json['monthly'][i]))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def get_lookback_stats(self, uuid, lookback) -> Player:
        if lookback>100:
            raise BadRequest("Can not look back more than 100 days!")
        try:
            async with aiohttp.request("GET", f"{self.api}/lookback?key={self.key}&uuid={uuid}&lookback={lookback}") as response:
                json = await response.json()
                if json['success']==True:
                    return Player(json, "lookback")
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def post_lookback_stats(self, uuids, lookback):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        if lookback>100:
            raise BadRequest("Can not look back more than 100 days!")
        try:
            async with aiohttp.request("POST", f"{self.api}/lookback?key={self.key}&days={lookback}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Player(json['lookback'][i]))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def get_history_stats(self, uuid, start, end) -> Player:
        try:
            async with aiohttp.request("GET", f"{self.api}/history?key={self.key}&uuid={uuid}&from={start}&to={end}") as response:
                json = await response.json()
                if json['success']==True:
                    if json['history']==[]:
                        return Player(DEFAULT)
                    days = []
                    for i in range(0, (end-start)-1):
                        days.append(Player(json['history'][i]))
                    return days
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def post_history_stats(self, uuids, start, end):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/history?key={self.key}&from={start}&to={end}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for u in uuids:
                        if json['history'][u]==[]:
                            players.append([Player(DEFAULT)])
                        else:
                            days = []
                            for i in range(0, (end-start)-1):
                                try:
                                    days.append(Player(json['history'][u][i]))
                                except:
                                    players.append(Player(DEFAULT))
                            players.append(days)
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)


    ###########################
    #                         #
    #      Leaderboards       #
    #                         #
    ###########################

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
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def get_ranking_stats(self, uuid, type, gamemode, stat) -> Ranking:
        try:
            async with aiohttp.request("GET", f"{self.api}/ranking?key={self.key}&uuid={uuid}&type={type}&gamemode={gamemode}&stat={stat}") as response:
                json = await response.json()
                if json['success']==True:
                    return Ranking(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
    
    async def post_ranking_stats(self, uuids, type, gamemode, stat):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/ranking?key={self.key}&type={type}&gamemode={gamemode}&stat={stat}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Ranking(json['ranking'][i], i))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)


    ###########################
    #                         #
    #          Misc           #
    #                         #
    ###########################
            
    async def get_formatted_stats(self, uuid) -> Formatted:
        try:
            async with aiohttp.request("GET", f"{self.api}/formatted?key={self.key}&uuid={uuid}") as response:
                json = await response.json()
                if json['success']==True:
                    return Formatted(json)
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    if json['cause']=="This player has not been registered with Observer!":
                        raise NotRegistered(uuid)
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def post_formatted_stats(self, uuids):
        if len(uuids)>16:
            raise BadRequest("You provided more than 16 uuids!")
        try:
            async with aiohttp.request("POST", f"{self.api}/formatted?key={self.key}", data={'uuids': uuids}) as response:
                json = await response.json()
                if json['success']==True:
                    players = []
                    for i in uuids:
                        players.append(Formatted(json['formatted'][i], i))
                    return players
                else:
                    if json['cause']=="Invalid API key":
                        raise InvalidAPIKeyError()
                    else:
                        raise APIError(json['cause'], response.status)
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)
            
    async def get_api_stats(self) -> Stats:
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
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)

    async def get_key_stats(self) -> Key:
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
        except aiohttp.ContentTypeError:
            raise APIError("error", 0)