class Stats:
    def __init__(self, data):
        self.data = data
        self.tracked_players = data.get("stats", {}).get("trackedPlayers", 0)
        self.commands_executed = data.get("stats", {}).get("commandsExecuted", 0)
        self.verified_users = data.get("stats", {}).get("verifiedUsers", 0)

class Key:
    def __init__(self, data):
        self.data = data
        self.key = data.get("record", {}).get("key", 0)
        self.owner = data.get("record", {}).get("owner", 0)
        self.limit = data.get("record", {}).get("limit", 0)
        self.minute_queries = data.get("record", {}).get("queriesInPastMin", 0)
        self.total_queries = data.get("record", {}).get("totalQueries", 0)
