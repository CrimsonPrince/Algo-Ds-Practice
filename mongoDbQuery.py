from pprint import pprint
from pymongo import MongoClient

client = MongoClient()
db=client.airplane_crashes
cursor = db.main2

result = cursor.find()

y = 0
data = {}

result = cursor.find({},{'_id' : 0})

for row in result:
	print(row)
