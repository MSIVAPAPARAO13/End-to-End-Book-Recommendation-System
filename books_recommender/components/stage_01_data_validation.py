import os
import sys
import pandas as pd
import pickle

from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.exception.exception_handler import AppException


class DataValidation:

    def __init__(self, app_config=AppConfiguration()):
        try:
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys)

    def preprocess_data(self):
        try:
            # 🔥 FIXED: handle bad rows
            ratings = pd.read_csv(
                self.data_validation_config.ratings_csv_file,
                sep=";",
                encoding='latin-1',
                on_bad_lines='skip'   # ✅ FIX
            )

            books = pd.read_csv(
                self.data_validation_config.books_csv_file,
                sep=";",
                encoding='latin-1',
                on_bad_lines='skip'   # ✅ FIX
            )

            logging.info(f"Ratings shape: {ratings.shape}")
            logging.info(f"Books shape: {books.shape}")

            # Select important columns
            books = books[['ISBN', 'Book-Title', 'Book-Author',
                           'Year-Of-Publication', 'Publisher', 'Image-URL-L']]

            # Rename columns
            books.rename(columns={
                "Book-Title": 'title',
                "Book-Author": 'author',
                "Year-Of-Publication": 'year',
                "Publisher": "publisher",
                "Image-URL-L": "image_url"
            }, inplace=True)

            ratings.rename(columns={
                "User-ID": 'user_id',
                "Book-Rating": 'rating'
            }, inplace=True)

            # Filter active users (>200 ratings)
            user_counts = ratings['user_id'].value_counts()
            active_users = user_counts[user_counts > 200].index
            ratings = ratings[ratings['user_id'].isin(active_users)]

            logging.info(f"After filtering users: {ratings.shape}")

            # Merge datasets
            ratings_books = ratings.merge(books, on='ISBN')

            # Count ratings per book
            num_rating = ratings_books.groupby('title')['rating'].count().reset_index()
            num_rating.rename(columns={'rating': 'num_of_rating'}, inplace=True)

            final_rating = ratings_books.merge(num_rating, on='title')

            # Keep books with >= 50 ratings
            final_rating = final_rating[final_rating['num_of_rating'] >= 50]

            # Remove duplicates
            final_rating.drop_duplicates(['user_id', 'title'], inplace=True)

            logging.info(f"Final dataset shape: {final_rating.shape}")

            # Save clean data
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)

            clean_path = os.path.join(
                self.data_validation_config.clean_data_dir,
                "clean_data.csv"
            )

            final_rating.to_csv(clean_path, index=False)
            logging.info(f"Saved clean data: {clean_path}")

            # Save pickle
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)

            pickle_path = os.path.join(
                self.data_validation_config.serialized_objects_dir,
                "final_rating.pkl"
            )

            with open(pickle_path, 'wb') as f:
                pickle.dump(final_rating, f)

            logging.info(f"Saved pickle: {pickle_path}")

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20} Data Validation Started {'='*20}")
            self.preprocess_data()
            logging.info(f"{'='*20} Data Validation Completed {'='*20}\n")

        except Exception as e:
            raise AppException(e, sys)