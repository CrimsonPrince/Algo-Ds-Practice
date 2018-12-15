import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
import math
client = MongoClient()
db=client.airplane_crashes

if client.drop_database('airplane_crashes'):
	print("Dropped Old Table")

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
df['Operator'] = df['Operator'].fillna("Unknown")
records = df.to_dict(orient = 'records')
operatorDict = {}


for items in records:
	operatorDict = {}
	operatorDict['Operator'] = items['Operator']
	try:
		db.newFormat.insert(operatorDict)
	except pymongo.errors.BulkWriteError as e:
		print(e.details['writeErrors'])

for items in records:
	crash = {}
	crash['type'] = items['Type']
	crash['location'] = items['Location']
	crash['date'] = items['Date']

	myquery = { "Operator": items['Operator'] }
	newvalues = { "$set": { "Crash": crash } }

	db.newFormat.update_one(myquery, newvalues)




pprint(db.newFormat.find_one())

#for i in insertionList:
	#print(i)
