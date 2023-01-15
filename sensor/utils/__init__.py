import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os, sys

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    """
    This function returns all the collections as a dataframe stored in Mongo DB
    database_name: Database Name
    collection_name: Collection Name
    =========================================================================
    return Pandas DataFrame of a collection
    """
    try:
        logging.info(f"Reading Data from Database: {database_name}, Collection: {collection_name} and converting it to DataFrame")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"DataFrame created successfully. Found columns: {df.columns}")
        if "_id" in df.columns:
            df.drop(labels="_id", axis=1, inplace=True)
        logging.info(f"Rows and Columns in DataFrame: {df.shape}")
        return df

    except Exception as e:
        logging.error(e)
        raise SensorException(e, sys)

