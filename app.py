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
            self.config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Load model + data safely
    def load_data(self):
        try:
            with open(self.config.trained_model_path, 'rb') as f:
                model = pickle.load(f)

            with open(self.config.book_pivot_serialized_objects, 'rb') as f:
                book_pivot = pickle.load(f)

            with open(self.config.final_rating_serialized_objects, 'rb') as f:
                final_rating = pickle.load(f)

            return model, book_pivot, final_rating

        except Exception:
            return None, None, None

    # 🔹 Recommendation logic
    def recommend_book(self, book_name):
        try:
            model, book_pivot, final_rating = self.load_data()

            if model is None:
                return [], []

            if book_name not in book_pivot.index:
                return [], []

            # Get index of selected book
            book_id = np.where(book_pivot.index == book_name)[0][0]

            # ✅ FIXED (no pandas error)
            distances, indices = model.kneighbors(
                book_pivot.iloc[book_id].values.reshape(1, -1),
                n_neighbors=6
            )

            indices = indices.flatten()

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

    # 🔹 Train model
    def train_model(self):
        try:
            pipeline = TrainingPipeline()
            pipeline.start_training_pipeline()
            st.success("✅ Training completed successfully!")
        except Exception as e:
            st.error("❌ Training failed")
            raise AppException(e, sys)

    # 🔹 Show recommendations
    def show_recommendations(self, book_name):
        books, posters = self.recommend_book(book_name)

        if not books:
            st.warning("⚠️ Train the model first or select a valid book.")
            return

        cols = st.columns(5)

        # Skip first (same book)
        for i in range(1, 6):
            with cols[i - 1]:
                st.text(books[i])
                st.image(posters[i])


# ================= STREAMLIT UI =================

if __name__ == "__main__":

    st.title("📚 Book Recommender System")
    st.write("KNN-based Collaborative Filtering")

    obj = Recommendation()

    # 🔹 Train button
    if st.button("🚀 Train Model"):
        obj.train_model()

    # 🔹 Load book names safely
    try:
        with open("artifacts/serialized_objects/book_names.pkl", "rb") as f:
            book_names = pickle.load(f)
            book_list = book_names.tolist()  # ✅ FIXED
    except:
        book_list = []

    if not book_list:
        book_list = ["No books available"]

    # 🔹 Dropdown
    selected_book = st.selectbox(
        "Select a book",
        book_list
    )

    # 🔹 Recommend button
    if st.button("📖 Show Recommendations"):
        obj.show_recommendations(selected_book)