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
result = cursor.find({'Crash.cnin': '47'}, {'Crash.cnin':1})
result = cursor.find({ "Crash" : { "$elemMatch" : { "cnin" : "47"} }})

agr = [ {'$group': {'_id': 1, 'all': { '$sum': '$Crash.in_Air' } } } ]

val = list(db.newFormat.aggregate(agr))


db.newFormat.find(
	{
		'Crash.cnin': '47'
	},
	{
		'Crash.cnin.$': 1,
		 name: 1
	}
)

db.newFormat.aggregate([{$group : {_id : "$Crash.type", num_tutorial : {$sum : "$Crash.in_Air"}}}]
db.newFormat.aggregate([{$group : {_id : "$Type", num_tutorial : {$avg : "$in_Air"}}}])


#db.newFormat.aggregate([{$match: {"Operator": "Military - U.S. Army"} },{$unwind: '$Crash'},{$group: {_id: null, "Sum": {$sum: "$Crash.in_Air" }}}])


#db.collection.aggregate( [{ $unwind: "$Crash" },{$group: {_id: {title: '$type'},SumOfDeaths: { $sum: '$crash.in_Air' }}},{$project: {_id: 0,title: '$_id.type',SumOfDeaths: 1}}]);



db.newFormat.aggregate( [{ $unwind: "$Crashes" },{$group: {_id: {title: '$type'},SumOfDeaths: { $sum: '$Crashes.in_Air' }}},{$project: {_id: 0,title: '$_id.type',SumOfDeaths: 1}}])
#print('The sum of prices is {}'.format(val[0]['all']))
#result = cursor.find({"Plane.type":"Zeppelin L-53 (airship)"})

#pipeline = [{"$match": {"operator": "Aer Lingus"}}, { "$group": {"_id": "$aboard","TotalDeaths": { "$sum": "$total" }}}]
#result = cursor.aggregate(pipeline)

#result = cursor.find_one({},{'_id' : 0})

result2 = list(result)
pprint(result2)

#for row in result:
	#pprint(row)
