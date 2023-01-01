import pymongo
import pandas as pd
import json 

# Providing the mongo localhost url to connect pyhton with mongo db

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME ="aps"
COLLECTION_NAME ="sensor"