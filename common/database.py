import os
import pymongo
from typing import Dict


class Database:
    URI = os.environ.get("MONGOLAB_URI")
    DATABASE = None

    @staticmethod
    def insert(collection: str, data: Dict):
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict, data: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)