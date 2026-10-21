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

    @staticmethod
    def insert_document(document):
        collection = MongoDBCommands.connect_to_mongodb()["reviews"]
        result = collection.insert_one(document)
        return result.inserted_id

    @staticmethod
    def find_documents(query):
        collection = MongoDBCommands.connect_to_mongodb()["reviews"]
        documents = collection.find(query)
        return list(documents)

    @staticmethod
    def update_document(query, update):
        collection = MongoDBCommands.connect_to_mongodb()["reviews"]
        result = collection.update_one(query, {'$set': update})
        return result.modified_count

    @staticmethod
    def delete_document(query):
        collection = MongoDBCommands.connect_to_mongodb()["reviews"]
        result = collection.delete_one(query)
        return result.deleted_count
    
    @staticmethod
    def close_connection():
        if MongoDBCommands._client is not None:
            MongoDBCommands._client.close()
            MongoDBCommands._client = None
            MongoDBCommands._db = None