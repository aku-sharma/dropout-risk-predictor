import streamlit as st
import requests

st.title("Student Dropout Risk Predictor")

attendance = st.slider("Attendance %", 0, 100, 80)
marks = st.slider("Marks %", 0, 100, 75)
backlogs = st.number_input("Backlogs", 0, 10, 0)
study_hours = st.slider("Study Hours", 0, 12, 4)
stress_level = st.slider("Stress Level", 1, 5, 2)

if st.button("Predict"):
    data = {
        "attendance": attendance,
        "marks": marks,
        "backlogs": backlogs,
        "study_hours": study_hours,
        "stress_level": stress_level
    }

    response = requests.post("http://127.0.0.1:5001/predict", json=data)
    result = response.json()

    st.success(f"Prediction: {result['prediction']}")