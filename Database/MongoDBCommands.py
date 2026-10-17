import pymongo

class MongoDBCommands:
    _client = None
    _db = None
    
    @staticmethod
    def connect_to_mongodb():
        if MongoDBCommands._client is None:
            MongoDBCommands._client = pymongo.MongoClient("localhost", 27017)
            MongoDBCommands._db = MongoDBCommands._client["electronic_store"]
        return MongoDBCommands._db
    
    def insert_document(self, document):
        collection = self.db["reviews"]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_documents(self, query):
        collection = self.db["reviews"]
        documents = collection.find(query)
        return list(documents)

    def update_document(self, query, update):
        collection = self.db["reviews"]
        result = collection.update_one(query, {'$set': update})
        return result.modified_count

    def delete_document(self, query):
        collection = self.db["reviews"]
        result = collection.delete_one(query)
        return result.deleted_count
    
    def close_connection(self):
        if MongoDBCommands._client is not None:
            MongoDBCommands._client.close()
            MongoDBCommands._client = None
            MongoDBCommands._db = None