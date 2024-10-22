from pymongo import MongoClient


class MongoDB_Session():
    def __init__(self, database, collection):
        # MongoDB connection
        self.client = MongoClient("mongodb://localhost:27017")
        self.database = self.client[database]  # Use your preferred database name
        self.collection = self.database[collection]  # Collection name
    
    def create(self, item: any):
        self.collection.insert_one(item.dict(exclude={"id"}))
    
    def fetch_all(self):
        items = []
        for item in self.collection.find(): # TODO add items helper
            items.append(item)
        return items
    
    def fetch_one(self, query: dict):
        return self.collection.find_one(query)
        