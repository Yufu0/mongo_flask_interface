from pymongo import MongoClient

class mongoDBConnector:
    def __init__(self):
        self.client = None
        self.connect()
        # print(self.client)
        print(self.find_all('music'))

    def find_all(self, collection_name):
        collection = self.client[collection_name]
        print(collection)
        music = []
        print(collection.find())
        for item in collection.find():
            print(item)
            music.append(
                {
                    'title': item.get('trackName'),
                    'artist': item.get('artistName'),
                    'duration': item.get('duration_ms')
                }
            )
        return music

    def connect(self):
        username = "username"
        password = "password"
        database = "spotify"
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = f"mongodb://{username}:{password}@localhost:27017/"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient('mongodb://username:password@localhost:27017/?authMechanism=DEFAULT')

        print(client)

        # Create the database for our example (we will use the same database throughout the tutorial
        self.client = client[database]