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

try:
	result = db.newFormat.insert(operatorList)
except pymongo.errors.BulkWriteError as e:
	print(e.details['writeErrors'])

result = db.newFormat.find()

for items in records:
	crash = {}
	crash['type'] = items['Type']
	crash['location'] = items['Location']
	crash['date'] = items['Date']

	for row in result:
		if row['Operator'] is items['Operator']:
			row['Crash'].append(crash)
		print(row['Operator'])



	db.newFormat.insert(crash)




pprint(db.newFormat.find_one())

#for i in insertionList:
	#print(i)
