class Daily:
    def __init__(self, data):
        self.data = data
        self.player = Player(data, 'daily')

class Weekly:
    def __init__(self, data):
        self.data = data
        self.player = Player(data, 'weekly')

class Monthly:
    def __init__(self, data):
        self.data = data
        self.player = Player(data, 'monthly')

class Lookback:
    def __init__(self, data):
        self.data = data
        self.player = Player(data, 'lookback')

class Formatted:
    def __init__(self, data):
        self.formatted = data.get("formatted", {})

class Player:
    def __init__(self, data, api:str):
        self.data = data
        
        self.timestamp = data.get(api, {}).get("timestamp", 0)
        self.wins = data.get(api, {}).get("wins", 0)
        self.coins = data.get(api, {}).get("coins", 0)
        self.karma = data.get(api, {}).get("karma", 0)
        self.achievementPoints = data.get(api, {}).get("achievementPoints", 0)
        self.experience = data.get(api, {}).get("experience", 0)
        self.quests = data.get(api, {}).get("quests", 0)
        self.challenges = data.get(api, {}).get("challenges", 0)
        self.reset = data.get(api, {}).get("reset", {})

        self.arenabrawl = ArenaBrawl(data.get(api, {}).get("stats", {}).get("arenabrawl", {}))
        self.bedwars = Bedwars(data.get(api, {}).get("stats", {}).get("bedwars", {}))
        self.blitz = Blitz(data.get(api, {}).get("stats", {}).get("blitzsurvivalgames", {}))
        self.buildbattle = BuildBattle(data.get(api, {}).get("stats", {}).get("buildbattle", {}))
        self.copsandcrims = CopsandCrims(data.get(api, {}).get("stats", {}).get("copsandcrims", {}))
        self.duels = Duels(data.get(api, {}).get("stats", {}).get("duels", {}))
        self.megawalls = MegaWalls(data.get(api, {}).get("stats", {}).get("megawalls", {}))
        self.murdermystery = MurderMystery(data.get(api, {}).get("stats", {}).get("murdermystery", {}))
        self.paintball = Paintball(data.get(api, {}).get("stats", {}).get("paintball", {}))
        self.quakecraft = Quakecraft(data.get(api, {}).get("stats", {}).get("quakecraft", {}))
        self.skywars = Skywars(data.get(api, {}).get("stats", {}).get("skywars", {}))
        self.smashheroes = SmashHeroes(data.get(api, {}).get("stats", {}).get("smashheroes", {}))
        self.speeduhc = SpeedUHC(data.get(api, {}).get("stats", {}).get("speeduhc", {}))
        self.tntgames = TntGames(data.get(api, {}).get("stats", {}).get("tntgame", {}))
        self.turbokart = TurboKart(data.get(api, {}).get("stats", {}).get("turbokartracers", {}))
        self.uhc = UHC(data.get(api, {}).get("stats", {}).get("uhc", {}))
        self.vampirez = VampireZ(data.get(api, {}).get("stats", {}).get("vampirez", {}))
        self.walls = Walls(data.get(api, {}).get("stats", {}).get("walls", {}))
        self.warlords = Warlords(data.get(api, {}).get("stats", {}).get("warlords", {}))

class ArenaBrawl:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        
class Bedwars:
    def __init__(self, data):
        self.level = data.get("level", 0)
        self.experience = data.get("experience", 0)
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.final_kills = data.get("final_kills", 0)
        self.final_deaths = data.get("final_deaths", 0)
        self.beds_broken = data.get("beds_broken", 0)
        self.beds_lost = data.get("beds_lost", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        self.four_v_four = Four_v_Four(data.get("4v4", {}))

class Four_v_Four:
    def __init__(self, data):
        self.wins = data.get("wins", 0)

class Blitz:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        self.time_played = data.get("time_played", 0)

class BuildBattle:
    def __init__(self, data):
        self.score = data.get("score", 0)
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.votes = data.get("votes", 0)

class CopsandCrims:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        self.round_wins = data.get("round_wins", 0)
        self.shots_fired = data.get("shots_fired", 0)
        self.headshot_kills = data.get("headshot_kills", 0)
        self.bombs_defused = data.get("bombs_defused", 0)
        self.bombs_planted = data.get("bombs_planted", 0)
        self.criminal_kills = data.get("criminal_kills", 0)
        self.cop_kills = data.get("cop_kills", 0)

class Duels:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        self.blocks_placed = data.get("blocks_placed", 0)
        self.goals = data.get("goals", 0)

class MegaWalls:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.assists = data.get("assists", 0)
        self.deaths = data.get("deaths", 0)
        self.final_kills = data.get("final_kills", 0)
        self.final_assists = data.get("final_assists", 0)
        self.final_deaths = data.get("final_deaths", 0)
        self.wither_damage = data.get("wither_damage", 0)
        self.defender_kills = data.get("defender_kills", 0)

class MurderMystery:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.murderer_wins = data.get("murderer_wins", 0)
        self.detective_wins = data.get("detective_wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class Paintball:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        
class Quakecraft:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)
        self.distance_travelled = data.get("distance_travelled", 0)

class Skywars:
    def __init__(self, data):
        self.experience = data.get("experience", 0)
        self.souls = data.get("souls", 0)
        self.time_played = data.get("time_played", 0)
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class SmashHeroes:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class SpeedUHC:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class TntGames:
    def __init__(self, data):
        self.wins = data.get("wins", 0)

class TurboKart:
    def __init__(self, data):
        self.trophies = Trophies(data.get("trophies", {}))
        self.wins = data.get("wins", 0)
        self.laps_completed = data.get("laps_completed", 0)
        self.boxes_picked_up = data.get("boxes_picked_up", 0)
        self.coins_picked_up = data.get("coins_picked_up", 0)

class Trophies:
    def __init__(self, data):
        self.gold = data.get("gold", 0)
        self.silver = data.get("silver", 0)
        self.bronze = data.get("bronze", 0)

class UHC:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.score = data.get("score", 0)
        self.heads_eaten = data.get("heads_eaten", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class VampireZ:
    def __init__(self, data):
        self.human = Human(data.get("human", {}))
        self.vampire = Vampire(data.get("vampire", {}))
        self.zombie_kills = data.get("zombie_kills", 0)

class Human:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class Vampire:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.kills = data.get("kills", 0)
        self.deaths = data.get("deaths", 0)

class Walls:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.assists = data.get("assists", 0)
        self.deaths = data.get("deaths", 0)

class Warlords:
    def __init__(self, data):
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.kills = data.get("kills", 0)
        self.assists = data.get("assists", 0)
        self.deaths = data.get("deaths", 0)
        self.damage_dealt = data.get("damage_dealt", 0)
        self.damage_taken = data.get("damage_taken", 0)
        self.damage_prevented = data.get("damage_prevented", 0)
        self.healed = data.get("healed", 0)