class Ranking:
    def __init__(self, data, uuid:str=""):
        self.data = data
        if uuid=="":
            self.rank = int(data.get("ranking", 0))
        else:
            self.rank = int(data)

# If you want to be able to get the leaderboard coresponding to the rank, tell me and I might add it here ;)