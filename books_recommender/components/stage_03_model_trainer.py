import os
import sys
import pickle

from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException


class ModelTrainer:

    def __init__(self, app_config=AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e, sys)

    def train(self):
        try:
            # Load pivot data
            with open(self.model_trainer_config.transformed_data_file_dir, 'rb') as f:
                book_pivot = pickle.load(f)

            logging.info(f"Loaded pivot data shape: {book_pivot.shape}")

            # Convert to sparse matrix
            book_sparse = csr_matrix(book_pivot)

            # Train KNN model
            model = NearestNeighbors(
                algorithm='brute',
                metric='cosine'   # IMPORTANT 🔥
            )

            model.fit(book_sparse)

            logging.info("Model training completed")

            # Save model
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)

            model_path = os.path.join(
                self.model_trainer_config.trained_model_dir,
                self.model_trainer_config.trained_model_name
            )

            with open(model_path, 'wb') as f:
                pickle.dump(model, f)

            logging.info(f"Model saved at: {model_path}")

        except Exception as e:
            raise AppException(e, sys)

    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20} Model Training Started {'='*20}")
            self.train()
            logging.info(f"{'='*20} Model Training Completed {'='*20}\n")

        except Exception as e:
            raise AppException(e, sys)