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

    # 🔹 Recommend Books
    def recommend_book(self, book_name):
        try:
            with open(self.recommendation_config.trained_model_path, 'rb') as f:
                model = pickle.load(f)

            with open(self.recommendation_config.book_pivot_serialized_objects, 'rb') as f:
                book_pivot = pickle.load(f)

            with open(self.recommendation_config.final_rating_serialized_objects, 'rb') as f:
                final_rating = pickle.load(f)

            # Check book exists
            if book_name not in book_pivot.index:
                return [], []

            # Get index
            book_id = np.where(book_pivot.index == book_name)[0][0]

            # Get recommendations
            distances, indices = model.kneighbors(
                book_pivot.iloc[book_id, :].values.reshape(1, -1),
                n_neighbors=6
            )

            indices = indices.flatten()   # 🔥 FIX (IMPORTANT)

            recommended_books = []
            posters = []

            for i in indices:
                title = book_pivot.index[i]
                recommended_books.append(title)

                idx = np.where(final_rating['title'] == title)[0][0]
                posters.append(final_rating.iloc[idx]['image_url'])

            return recommended_books, posters

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Train Pipeline
    def train_engine(self):
        obj = TrainingPipeline()
        obj.start_training_pipeline()
        st.success("Training Completed!")

    # 🔹 Display Results
    def show_recommendations(self, selected_book):
        books, posters = self.recommend_book(selected_book)

        if not books:
            st.error("Book not found!")
            return

        cols = st.columns(5)

        # Skip first (same book)
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

    selected_book = st.selectbox(
        "Select a book",
        book_names
    )

    # Recommend button
    if st.button("Show Recommendations"):
        obj.show_recommendations(selected_book)