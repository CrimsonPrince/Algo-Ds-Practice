from pymongo import MongoClient
import pandas as pd
from pprint import pprint
client = MongoClient()
db=client.airplane_crashes

df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv") #csv file which you want to import
records_ = df.to_dict(orient = 'record')
result = db.main.insert_many(records_)
pprint(db.main.find_one())
print("Inserted")
