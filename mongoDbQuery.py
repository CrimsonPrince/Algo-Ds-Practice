from pprint import pprint
from pymongo import MongoClient

client = MongoClient()
db=client.airplane_crashes
cursor = db.newFormat

result = cursor.find()

y = 0
data = {}


#result = cursor.find({},{'_id' : 0})
#result = cursor.find({'Operator':'Military - U.S. Army'},{'_id' : 0})
#result = cursor.find({'Operator':'Military - U.S. Army'},{'in_Air' : {'$gte':30}})

agr = [ {'$group': {'_id': 1, 'all': { '$sum': '$in_Air' } } } ]

val = list(db.newFormat.aggregate(agr))

print('The sum of prices is {}'.format(val[0]['all']))
#result = cursor.find({"Plane.type":"Zeppelin L-53 (airship)"})

#pipeline = [{"$match": {"operator": "Aer Lingus"}}, { "$group": {"_id": "$aboard","TotalDeaths": { "$sum": "$total" }}}]
#result = cursor.aggregate(pipeline)

#result = cursor.find_one({},{'_id' : 0})

#result2 = list(result)
#pprint(result2)

#for row in result:
	#pprint(row)
