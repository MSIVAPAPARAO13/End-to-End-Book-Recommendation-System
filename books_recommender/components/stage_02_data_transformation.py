import os
import sys
import pickle
import pandas as pd

from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException


class DataTransformation:

    def __init__(self, app_config=AppConfiguration()):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys)

    def get_data_transformer(self):
        try:
            # Load clean data
            df = pd.read_csv(self.data_transformation_config.clean_data_file_path)

            logging.info(f"Loaded clean data shape: {df.shape}")

            # Create pivot table
            book_pivot = df.pivot_table(
                columns='user_id',
                index='title',
                values='rating'
            )

            logging.info(f"Pivot table shape: {book_pivot.shape}")

            # Fill missing values
            book_pivot.fillna(0, inplace=True)

            # Save transformed data
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)

            transformed_path = os.path.join(
                self.data_transformation_config.transformed_data_dir,
                "transformed_data.pkl"
            )

            with open(transformed_path, 'wb') as f:
                pickle.dump(book_pivot, f)

            logging.info(f"Saved transformed data: {transformed_path}")

            # Extract book names
            book_names = book_pivot.index

            # Save serialized objects
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)

            book_names_path = os.path.join(
                self.data_validation_config.serialized_objects_dir,
                "book_names.pkl"
            )

            book_pivot_path = os.path.join(
                self.data_validation_config.serialized_objects_dir,
                "book_pivot.pkl"
            )

            with open(book_names_path, 'wb') as f:
                pickle.dump(book_names, f)

            with open(book_pivot_path, 'wb') as f:
                pickle.dump(book_pivot, f)

            logging.info("Saved book_names and book_pivot successfully")

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_transformation(self):
        try:
            logging.info(f"{'='*20} Data Transformation Started {'='*20}")
            self.get_data_transformer()
            logging.info(f"{'='*20} Data Transformation Completed {'='*20}\n")

        except Exception as e:
            raise AppException(e, sys)