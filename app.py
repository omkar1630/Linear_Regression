import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Machine Learning Prediction App")

# Example: Single input feature
feature = st.number_input("Enter Value")

if st.button("Predict"):
    prediction = model.predict([[feature]])
    st.success(f"Prediction: {prediction[0]}")
