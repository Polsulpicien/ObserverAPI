class APIError(Exception):
    def __init__(self, error, code):
        self.error = error
        self.status_code = code

class InvalidAPIKeyError(Exception):
    def __init__(self):
        self.error = "Invalid API key"

class HistoryLimitError(Exception):
    def __init__(self):
        self.error = "Can not look back more than 100 days!" 