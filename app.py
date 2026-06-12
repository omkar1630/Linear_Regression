import streamlit as st
import pickle
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="📚",
    layout="centered"
)

# Load Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("📚 Student Performance Prediction")
st.markdown(
    "Enter the student details below and predict the **Performance Index**."
)

# Inputs
hours_studied = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

papers_practiced = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    value=5
)

# Prediction Button
if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "Hours Studied": [hours_studied],
        "Previous Scores": [previous_scores],
        "Sleep Hours": [sleep_hours],
        "Sample Question Papers Practiced": [papers_practiced]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"🎯 Predicted Performance Index: {prediction:.2f}")

    if prediction >= 90:
        st.info("🏆 Performance Level: Excellent")
    elif prediction >= 75:
        st.info("👍 Performance Level: Good")
    elif prediction >= 60:
        st.info("📘 Performance Level: Average")
    else:
        st.info("📚 Performance Level: Needs Improvement")
