class Stats:
    def __init__(self, data):
        self.data = data
        self.trackedPlayers = data.get("stats", {}).get("trackedPlayers", 0)
        self.commandsExecuted = data.get("stats", {}).get("commandsExecuted", 0)
        self.verifiedUsers = data.get("stats", {}).get("verifiedUsers", 0)