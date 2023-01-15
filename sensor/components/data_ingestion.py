from sensor import utils
from sensor.entity import config_entity, artifact_entity
from sensor.logger import logging
from sensor.exception import SensorException
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            # Exporting Collection Data as Pandas Dataframe
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name, 
                collection_name=self.data_ingestion_config.collection_name)

            # save data in feature store
            df.replace(to_replace="na", value=np.NAN, inplace=True)

            # create feature store folder
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            # save df to feature store
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path, index=False, header=True)

            # Splitting the data into training & test set
            train_df, test_df = train_test_split(df, test_size=self.config_entity.DataIngestionConfig.test_size,
            random_state=)

        except Exception as e:
            raise SensorException(e, sys)

