import os
import sys
import pickle
import streamlit as st
import numpy as np

from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


class Recommendation:

    def __init__(self, app_config=AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Fetch Posters
    def fetch_poster(self, suggestions):
        try:
            with open(self.recommendation_config.book_pivot_serialized_objects, 'rb') as f:
                book_pivot = pickle.load(f)

            with open(self.recommendation_config.final_rating_serialized_objects, 'rb') as f:
                final_rating = pickle.load(f)

            book_names = [book_pivot.index[i] for i in suggestions[0]]

            poster_urls = []
            for name in book_names:
                idx = np.where(final_rating['title'] == name)[0][0]
                poster_urls.append(final_rating.iloc[idx]['image_url'])

            return poster_urls

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Recommendation Logic
    def recommend_book(self, book_name):
        try:
            with open(self.recommendation_config.trained_model_path, 'rb') as f:
                model = pickle.load(f)

            with open(self.recommendation_config.book_pivot_serialized_objects, 'rb') as f:
                book_pivot = pickle.load(f)

            if book_name not in book_pivot.index:
                return [], []

            book_id = np.where(book_pivot.index == book_name)[0][0]

            distances, suggestions = model.kneighbors(
                book_pivot.iloc[book_id, :].values.reshape(1, -1),
                n_neighbors=6
            )

            book_names = [book_pivot.index[i] for i in suggestions[0]]
            poster_urls = self.fetch_poster(suggestions)

            return book_names, poster_urls

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Train Pipeline
    def train_engine(self):
        obj = TrainingPipeline()
        obj.start_training_pipeline()
        st.success("Training Completed!")

    # 🔹 Display Recommendations
    def show_recommendations(self, selected_book):
        books, posters = self.recommend_book(selected_book)

        if not books:
            st.error("Book not found!")
            return

        cols = st.columns(5)

        for i in range(1, 6):
            with cols[i - 1]:
                st.text(books[i])
                st.image(posters[i])


# ================= UI =================

if __name__ == "__main__":

    st.title("📚 Book Recommender System")
    st.write("Collaborative Filtering using KNN")

    obj = Recommendation()

    # Train button
    if st.button("Train Model"):
        obj.train_engine()

    # Load book names
    with open("artifacts/serialized_objects/book_names.pkl", "rb") as f:
        book_names = pickle.load(f)

    selected_book = st.selectbox("Select a book", book_names)

    if st.button("Show Recommendations"):
        obj.show_recommendations(selected_book)