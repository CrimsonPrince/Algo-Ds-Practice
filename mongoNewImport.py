import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
from bson import *


client = MongoClient()
db=client.airplane_crashes

if client.drop_database('airplane_crashes'):
	print("Dropped Old Table")

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
df['Operator'] = df['Operator'].fillna("Unknown")
records = df.to_dict(orient = 'records')
operatorDict = []
spareDict = {}
operatorList = []


for items in records:
	if items['Operator'] not in operatorDict:
		spareDict = {}
		spareDict['Operator'] = items['Operator']
		spareDict['Crash'] = list()
		operatorDict.append(items['Operator'])
		operatorList.append(spareDict)
	output = db.newFormat.replace_one({"Operator": items['Operator']},insertDict)



try:
	result = db.newFormat.insert(operatorList)
except pymongo.errors.BulkWriteError as e:
	print(e.details['writeErrors'])

pprint(db.newFormat.find_one())

#for i in insertionList:
	#print(i)
