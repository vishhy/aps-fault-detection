import pymongo
import pandas as pd
import json 
from dataclasses import dataclass
import os

# Providing the mongo localhost url to connect pyhton with mongo db

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key:str = os.getenv("AWS_ACCESS_KEY")
    aws_secret_id:str = os.getenv("AWS_SECRET_ID")


env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)