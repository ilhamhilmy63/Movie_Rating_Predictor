import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🎬 Movie Rating Predictor")

st.write("Enter movie details to predict rating:")

runtime = st.number_input("Movie Runtime (minutes)", min_value=30, max_value=240, step=5)
budget = st.number_input("Budget (in million $)", min_value=1, max_value=500, step=1)
popularity = st.slider("Popularity Score", 0.0, 100.0, 10.0)
genre = st.selectbox("Genre", ["Action", "Comedy", "Drama", "Horror", "Romance"])

# Dummy encoding
genre_encoded = {"Action":0, "Comedy":1, "Drama":2, "Horror":3, "Romance":4}[genre]

if st.button("Predict Rating"):
    features = [[runtime, budget, popularity, genre_encoded]]
    prediction = model.predict(features)
    st.success(f"⭐ Predicted Rating: {prediction[0]:.2f}")
