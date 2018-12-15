from pprint import pprint
from mongoengine import *
import pandas as pd

class Operator(Document):
	name = StringField(max_length=20000)

class Crash(Document):
	Type = StringField(max_length=20000)
	Date = StringField(max_length=20000)
	Location = StringField(max_length=20000)
	OperatorName = ReferenceField(Operator)


connect('airplane_crashes')


df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
df['Operator'] = df['Operator'].fillna("Unknown")
records = df.to_dict(orient = 'records')
operatorDict = {}


for row in records:
	if row['Operator'] not in operatorDict:
		operator = Operator(name = row['Operator'])
		operator.save()
		operatorDict[row['Operator']] = list()

	crash = Crash(Type = str(row['Type']), Date = str(row['Date']), Location = str(row['Location']), OperatorName = row['Operator'])
	crash.save()

"""for operator in Operator.objects:
	pprint(Crash.objects(OperatorName__all=[]))"""
