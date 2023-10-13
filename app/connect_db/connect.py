from pymongo import MongoClient
import os

class mongoDBConnector:
    def __init__(self):
        self.client = None
        self.connect()

    def find_all(self, collection_name):
        collection = self.client[collection_name]
        music = []
        for item in collection.find():
            if item is not None and item.get('trackName') is not None and item.get('artistName') is not None and item.get('duration_ms') is not None:
                music.append(
                    {
                        'title': item.get('trackName'),
                        'artist': item.get('artistName'),
                        'duration': item.get('duration_ms')
                    }
                )
        return music
    
    def recherche(self, collection_name, rech):
        collection = self.client[collection_name]
        music = []
        for item in collection.find({'artistName': rech}):
            if item is not None and item.get('trackName') is not None and item.get('artistName') is not None and item.get('duration_ms') is not None:
                music.append(
                    {
                        'title': item['trackName'],
                        'artist': item['artistName'],
                        'duration': item['duration_ms']
                    }
                )
        return music

    def connect(self):
        username = os.environ["MONGO_USERNAME"]
        password = os.environ["MONGO_PASSWORD"]
        database = os.environ["MONGO_DATABASE"]
        address = os.environ["MONGO_ADDRESS"]
        port = os.environ["MONGO_PORT"]
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = f"mongodb://{username}:{password}@{address}:{port}/"
        print(CONNECTION_STRING)

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)

        # Create the database for our example (we will use the same database throughout the tutorial
        self.client = client[database]
