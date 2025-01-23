# data_cache.py

class DataCache:
    def __init__(self):
        self.data = {}

    def update(self, topic, payload):
        self.data[topic] = payload

    def get_latest_data(self):
        return self.data
