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
i = 0


for items in records:
	crash = {}
	plane = {}
	operator = {}
	planeList = []


	if str(items['Operator']) not in operatorDict:
		operatorDict[items['Operator']] = list()

	#operator['operator'] = items['Operator']
	crash['flight_Number'] = items['Flight #']
	crash['route'] = items['Route']
	crash['aboard'] = items['Aboard']
	crash['summary'] = items['Summary']

	crash['type'] = items['Type']
	crash['cnin'] = items['cn/In']
	crash['registration'] = items['Registration']
	operator['crash'] = crash

	crash['date'] = items['Date']
	crash['Time'] = items['Time']
	crash['location'] = items['Location']
	crash['in_Air'] = items['Fatalities']
	crash['on_Ground'] = items['Ground']

	operator['crash'] = crash


	operatorDict[items['Operator']].append(operator)

for row, key in operatorDict.items():
	f = dict()
	f[row] = key
	try:
		db.newFormat.insert(f,check_keys=False)
	except pymongo.errors.BulkWriteError as e:
		print(e.details['writeErrors'])

pprint(db.newFormat.find_one({}, {'_id':0}))

#for i in insertionList:
	#print(i)
