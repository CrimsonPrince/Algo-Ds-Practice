import pprint
from pymongo import MongoClient

client = MongoClient()
db=client.olympics
olympics = db.games

result = olympics.find()
i = 0
