import pymongo

class MongoConnection:
    def __init__(self, db_name, host='localhost', port=27017):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]
