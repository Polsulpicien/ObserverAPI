class APIError(Exception):
    def __init__(self, error, code):
        self.error = error
        self.status_code = code

class InvalidAPIKeyError(Exception):
    def __init__(self):
        self.error = "Invalid API key"

class NotRegistered(Exception):
    def __init__(self, player):
        self.error = f"Player not Registered: {player}"
        self.player = player

class BadRequest(Exception):
    def __init__(self, error):
        self.error = error