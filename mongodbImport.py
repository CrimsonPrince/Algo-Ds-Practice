from pymongo import MongoClient
import pandas as pd
import pprint
client = MongoClient()
db=client.olympics

df = pd.read_csv("ign.csv") #csv file which you want to import
records_ = df.to_dict(orient = 'records')
#print(records_[1])
result = db.games.insert_many(records_)

print(result.inserted_ids)
