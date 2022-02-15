class Ranking:
    def __init__(self, data):
        self.data = data
        self.rank = data.get("ranking", 0)

    # will be improved in the future...