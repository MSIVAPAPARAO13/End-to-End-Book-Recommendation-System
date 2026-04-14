import sys

from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException

from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.components.stage_01_data_validation import DataValidation
from books_recommender.components.stage_02_data_transformation import DataTransformation
from books_recommender.components.stage_03_model_trainer import ModelTrainer


class TrainingPipeline:

    def __init__(self):
        try:
            # Initialize all stages
            self.data_ingestion = DataIngestion()
            self.data_validation = DataValidation()
            self.data_transformation = DataTransformation()
            self.model_trainer = ModelTrainer()

        except Exception as e:
            raise AppException(e, sys)

    def start_training_pipeline(self):
        """
        Runs the full ML pipeline step-by-step
        """
        try:
            logging.info(f"{'='*20} TRAINING PIPELINE STARTED {'='*20}")

            # Step 1: Data Ingestion
            logging.info("Starting Data Ingestion...")
            self.data_ingestion.initiate_data_ingestion()

            # Step 2: Data Validation
            logging.info("Starting Data Validation...")
            self.data_validation.initiate_data_validation()

            # Step 3: Data Transformation
            logging.info("Starting Data Transformation...")
            self.data_transformation.initiate_data_transformation()

            # Step 4: Model Training
            logging.info("Starting Model Training...")
            self.model_trainer.initiate_model_trainer()

            logging.info(f"{'='*20} TRAINING PIPELINE COMPLETED {'='*20}\n")

        except Exception as e:
            raise AppException(e, sys)