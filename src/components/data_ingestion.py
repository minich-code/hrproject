import os
import sys
import pandas as pd
from src.exception import FileOperationError
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method')

        try:
            # Read the dataset into a DataFrame
            df = pd.read_csv(r"E:\MLproject\hrproject\notebook\data\Performance.csv")
            logging.info("Dataset read successfully")

            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw dataset saved")

            # Split the dataset into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)

            # Save the train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train-test split completed")

            # Return paths to train and test sets
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            # Raise custom exception for file operations
            raise FileOperationError(e, sys)


if __name__ == "__main__":
    # Instantiate DataIngestion class and initiate data ingestion
    obj = DataIngestion()
    obj.initiate_data_ingestion()
        