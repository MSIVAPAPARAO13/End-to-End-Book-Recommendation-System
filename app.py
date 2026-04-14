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

    # 🔹 Fetch Poster Images
    def fetch_poster(self, suggestions):
        try:
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_objects, 'rb'))

            book_names = [book_pivot.index[i] for i in suggestions[0]]

            poster_urls = []
            for name in book_names:
                idx = np.where(final_rating['title'] == name)[0][0]
                url = final_rating.iloc[idx]['image_url']
                poster_urls.append(url)

            return book_names, poster_urls

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 Recommend Books
    def recommend_book(self, book_name):
        try:
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))

            if book_name not in book_pivot.index:
                return [], []

            book_id = np.where(book_pivot.index == book_name)[0][0]

            distances, suggestions = model.kneighbors(
                book_pivot.iloc[book_id, :].values.reshape(1, -1),
                n_neighbors=6
            )

            return self.fetch_poster(suggestions)

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

        for i in range(1, 6):  # skip first (same book)
            with cols[i-1]:
                st.text(books[i])
                st.image(posters[i])


# ================= STREAMLIT UI =================

if __name__ == "__main__":

    st.title("📚 Book Recommender System")
    st.write("Collaborative Filtering using KNN")

    obj = Recommendation()

    # 🔹 Train Button
    if st.button("Train Model"):
        obj.train_engine()

    # 🔹 Load book names (FIXED PATH 🔥)
    book_names = pickle.load(
        open("artifacts/serialized_objects/book_names.pkl", "rb")
    )

    selected_book = st.selectbox(
        "Select a book",
        book_names
    )

    # 🔹 Recommend Button
    if st.button("Show Recommendations"):
        obj.show_recommendations(selected_book)