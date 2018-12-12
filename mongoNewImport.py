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


i = 0
insertionList = list()

for items in records:
	data = {}
	plane = {}
	crash = {}
	deaths = {}

	data['flight_Number'] = items['Flight #']
	data['route'] = items['Route']
	data['operator'] = items['Operator']
	data['aboard'] = items['Aboard']
	data['summary'] = items['Summary']

	plane['type'] = items['Type']
	plane['cnin'] = items['cn/In']
	plane['registration'] = items['Registration']
	data['Plane'] = plane

	crash['date'] = items['Date']
	crash['Time'] = items['Time']
	crash['location'] = items['Location']
	deaths['in_Air'] = items['Fatalities']
	deaths['on_Ground'] = items['Ground']

	crash['deaths'] = deaths
	data['crash'] = crash

	try:
		db.newFormat.insert_one(data)
	except pymongo.errors.BulkWriteError as e:
		print(e.details['writeErrors'])

#for i in insertionList:
	#print(i)
