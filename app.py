import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Performance Prediction")

hours_studied = st.number_input("Hours Studied", min_value=0.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0)
papers_practiced = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0
)

if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [papers_practiced]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Performance Index: {prediction[0]:.2f}"
    )
