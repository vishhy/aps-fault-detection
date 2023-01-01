import pandas as pd
import pymongo
import json
from dataclasses import dataclass
import os,sys   
# Provide the localhost url to connect mongo db to pyhon

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key:str = os.getenv("AWS_ACCESS_KEY")
    aws_secret_id:str = os.getenv("AWS_SECRET_ID")

env_var = EnvironmentVariable()
client = pymongo.MongoClient(env_var.mongo_db_url)

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    pass
