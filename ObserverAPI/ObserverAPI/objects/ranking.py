class Ranking:
    def __init__(self, data):
        self.data = data
        self.rank = int(data.get("ranking", 0))

    # will be improved in the future... or not.