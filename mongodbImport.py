import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["olympics"]

print(myclient.list_database_names())

participant = mydb['participant']

import csv
with open('ign.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for i in range(10):
		print(reader[i])
