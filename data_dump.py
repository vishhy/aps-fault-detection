import pymongo
import pandas as pd
import json 

# Providing the mongo localhost url to connect pyhton with mongo db

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME ="aps"
COLLECTION_NAME ="sensor"

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)

    print(f"Rows and columns: {df.shape}")

    # Converting df to json so that we can dump it into mongo db since mongo db wants json format
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    # Inserting into mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    # origin is only a variable, we can name the remote variable as anything as we want
    # git add remote repo_link https://github.com/vishhy/aps-fault-detection.git

# Input to ML by Ineuron: Configuration
# Output geenrated by ML Training Pipeline by Industry in the form of Trained Model, Training Milestone or file: Artifact
