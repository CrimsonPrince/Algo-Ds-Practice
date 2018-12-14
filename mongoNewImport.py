import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
client = MongoClient()
db=client.airplane_crashes

if client.drop_database('airplane_crashes'):
	print("Dropped Old Table")

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
records = df.to_dict(orient = 'records')

for items in records:
	crash = {}
	plane = {}
	operator = {}
	planeList = []

	crash['flight_Number'] = items['Flight #']
	crash['route'] = items['Route']
	operator['operator'] = items['Operator']
	crash['aboard'] = items['Aboard']
	crash['summary'] = items['Summary']

	plane['type'] = items['Type']
	plane['cnin'] = items['cn/In']
	plane['registration'] = items['Registration']
	planeList.append(plane)
	crash['Plane'] = planeList
	operator['crash'] = crash

	crash['date'] = items['Date']
	crash['Time'] = items['Time']
	crash['location'] = items['Location']
	crash['in_Air'] = items['Fatalities']
	crash['on_Ground'] = items['Ground']

	operator['crash'] = crash

	try:
		db.newFormat.insert(operator)
	except pymongo.errors.BulkWriteError as e:
		print(e.details['writeErrors'])

#for i in insertionList:
	#print(i)
