class APIError(Exception):
    def __init__(self, error, code):
        self.error = error
        self.status_code = code

class HistoryLimitError(Exception):
    def __init__(self):
        self.error = "Can not look back more than 100 days!"