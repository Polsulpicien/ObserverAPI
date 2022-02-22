class Leaderboards:
    def __init__(self, data):
        self.data = data
        self.success = data.get("success", {})
        self.leaderboard = data.get("leaderboards", {})

    def get_index(self, index:int):
        return Index(self.leaderboard, index-1)

class Index:
    def __init__(self, data, index):
        self.rank = data[index].get("rank", 0)
        self.id = data[index].get("id", 0)
        self.value = data[index].get("value", 0)
        self.formatted = data[index].get("formatted", "") 
