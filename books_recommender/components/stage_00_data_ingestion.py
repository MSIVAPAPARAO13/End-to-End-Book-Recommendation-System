import os
import sys
from six.moves import urllib
import zipfile

from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration


class DataIngestion:

    def __init__(self, app_config=AppConfiguration()):
        try:
            logging.info(f"{'='*20} Data Ingestion Started {'='*20}")
            self.data_ingestion_config = app_config.get_data_ingestion_config()
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            os.makedirs(raw_data_dir, exist_ok=True)

            file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Downloading data from {dataset_url}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)

            logging.info(f"Downloaded file at {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys)

    def extract_zip_file(self, zip_file_path: str):
        try:
            ingested_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(ingested_dir, exist_ok=True)

            logging.info(f"Extracting {zip_file_path} into {ingested_dir}")

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)

            logging.info("Extraction completed")

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path)

            logging.info(f"{'='*20} Data Ingestion Completed {'='*20}\n")

        except Exception as e:
            raise AppException(e, sys)