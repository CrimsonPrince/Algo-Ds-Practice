from pprint import pprint
from mongoengine import *
import pandas as pd

class Crash(EmbeddedDocument):
	Type = StringField(max_length=20000)
	Date = StringField(max_length=20000)
	Location = StringField(max_length=20000)

class Operator(Document):
	name = StringField(max_length=20000)
	crashes = ListField(EmbeddedDocumentField(Crash))


connect('airplane_crashes')


df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
df['Operator'] = df['Operator'].fillna("Unknown")
records = df.to_dict(orient = 'records')

operatorDict = {}

for row in records:
	operator = Operator(name = row['Operator'])
	operator.save()

	if row['Operator'] not in operatorDict:
		operatorDict[row['Operator']] = list()

for operator in Operator.objects:
	print(operator.name)
