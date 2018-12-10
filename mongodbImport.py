from pymongo import MongoClient
import pandas as pd
import pprint
client = MongoClient()
db=client.test
games = db.games
df = pd.read_csv("ign.csv") #csv file which you want to import
records_ = df.to_dict(orient = 'records')
#print(records_[1])
result = db.employee.insert_many(records_)

x = db.employee.find_one()
print(x)
