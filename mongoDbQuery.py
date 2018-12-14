from pprint import pprint
from pymongo import MongoClient

client = MongoClient()
db=client.airplane_crashes
cursor = db.newFormat

result = cursor.find()

y = 0
data = {}

result = cursor.find({},{'_id' : 0})

result = cursor.find({"Plane.type":"Zeppelin L-53 (airship)"})

pipeline = [{"$match": {"operator": "Aer Lingus"}}, { "$group": {"_id": "$aboard","TotalDeaths": { "$sum": "$total" }}}]
result = cursor.aggregate(pipeline)

result = cursor.find_one({},{'_id' : 0})

result2 = list(result)
pprint(result)

#for row in result:
	#pprint(row)
