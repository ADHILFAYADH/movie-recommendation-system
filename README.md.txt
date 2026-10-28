# Movie Recommendation System

## Project Overview
This project recommends movies based on the similarity between movie descriptions and selected features.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit

## How It Works
1. Load movie data from a CSV file.
2. Process selected movie features.
3. Convert text features into numerical vectors using TF-IDF.
4. Calculate similarity scores using cosine similarity.
5. Recommend similar movies based on the selected movie.

## How to Run the Project
1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the required libraries:

   `pip install -r requirements.txt`

5. Start the Streamlit application:

   `python -m streamlit run app.py`

## Project Files
- `app.py` — Streamlit application.
- `movies.csv` — Movie dataset, if included in the repository.
- `requirements.txt` — Python dependencies.

## Learning Outcomes
- Data preprocessing with Pandas.
- Text vectorization using TF-IDF.
- Similarity calculation using cosine similarity.
- Building a simple web application with Streamlit.