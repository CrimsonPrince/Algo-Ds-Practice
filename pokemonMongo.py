import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint

client = MongoClient()
db=client.pokedex

if client.drop_database('pokedex'):
	print("Dropped Old Table")

df = pd.read_csv("pokemon.csv") #csv file which you want to import
records = df.to_dict(orient = 'records')


for items in records:
	pokemon = {}
	stats = {}
	type = {}

	pokemon['name'] = items['Name']
	pokemon['total'] = items['Total']
	pokemon['Legendary'] = items['Legendary']
	pokemon['generation'] = items['Generation']

	type['type 1'] = items['Type 1']
	type['type 2'] = items['Type 2']
	pokemon['type'] = type

	stats['hp'] = items['HP']
	stats['attack'] = items['Attack']
	stats['defense'] = items['Defense']
	stats['SpAtk'] = items['Sp. Atk']
	stats['SpDef'] = items['Sp. Def']
	stats['speed'] = items['Speed']

	pokemon['stats'] = stats




	try:
		db.newFormat.insert_one(pokemon)
	except pymongo.errors.BulkWriteError as e:
		print(e.details['writeErrors'])

#for i in insertionList:
	#print(i)
