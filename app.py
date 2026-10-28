import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies_data = pd.read_csv("movies.csv")

# Select features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Replace missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# TF-IDF
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine similarity
similarity = cosine_similarity(feature_vectors)


# ---------------- UI ----------------

st.title("📽️ Movie Recommendation System")

movie_name = st.text_input("Enter Your Favourite Movie")

if st.button("Recommend Movies"):

    list_titles = movies_data['title'].tolist()

    final_close_match = difflib.get_close_matches(
        movie_name,
        list_titles
    )

    if not final_close_match:

        st.error("Sorry, this movie is not available in our dataset.")

    else:

        close_match = final_close_match[0]
        

        st.write("Recommendations based on:", close_match)

        index_of_the_movie = movies_data[
            movies_data.title == close_match
        ]['index'].values[0]

        similarity_score = list(
            enumerate(similarity[index_of_the_movie])
        )

        sorted_similar_movies = sorted(
            similarity_score,
            key=lambda x: x[1],
            reverse=True
        )

        st.subheader("Suggested Movies For You:")

        i = 1

        for movie in sorted_similar_movies:

            index = movie[0]

            title_from_index = movies_data[
                movies_data.index == index
            ]['title'].values[0]

            if i <= 30:

                st.write(f"{i}. {title_from_index}")

                i += 1