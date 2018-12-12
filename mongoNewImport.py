from pymongo import MongoClient
import pandas as pd
from pprint import pprint
client = MongoClient()
db=client.airplane_crashes

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
records = df.to_dict(orient = 'records')

data = {}
plane = {}
crash = {}
deaths = {}

for items in records:
	data['flight_Number'] = items['Flight #']
	data['route'] = items['Route']
	data['operator'] = items['Operator']
	data['aboard'] = items['Aboard']

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
	print(data)
