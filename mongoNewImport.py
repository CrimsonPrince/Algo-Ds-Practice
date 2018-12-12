from pymongo import MongoClient
import pandas as pd
from pprint import pprint
client = MongoClient()
db=client.airplane_crashes

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
records_ = df.to_dict(orient = 'records')
for key, items in records.items():
	print(items['Date'])

"""data = {}
plane = {}

data['Date'] = 12
data['Name'] = "Arthur"
plane['age'] = 10
plane['Year'] = 1194
data['Plane'] = plane

result = db.main2.insert_one(data)"""
