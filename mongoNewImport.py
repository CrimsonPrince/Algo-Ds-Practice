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
insertionList = list()

for items in records:
	crash = {}
	deaths = {}
	operator = {}

	crash['flight_Number'] = items['Flight #']
	crash['route'] = items['Route']
	operator['operator'] = items['Operator']
	crash['aboard'] = items['Aboard']
	crash['summary'] = items['Summary']

	crash['type'] = items['Type']
	crash['cnin'] = items['cn/In']
	crash['registration'] = items['Registration']
	operator['crash'] = crash

	crash['date'] = items['Date']
	crash['Time'] = items['Time']
	crash['location'] = items['Location']
	deaths['in_Air'] = items['Fatalities']
	deaths['on_Ground'] = items['Ground']

	crash['deaths'] = deaths
	operator['crash'] = crash

	insertionList.append(operator)

try:
	db.newFormat.insert_many(insertionList)
except pymongo.errors.BulkWriteError as e:
	print(e.details['writeErrors'])

#for i in insertionList:
	#print(i)
