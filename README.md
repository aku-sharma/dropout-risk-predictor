# 🎓 Student Dropout Risk Predictor

A Machine Learning-based web application that predicts the risk of student dropout based on academic and behavioral factors.

---

## 🚀 Live Demo
👉 Frontend: https://dropout-risk-predictor-fzsah7b3abvhr9kakg9dxa.streamlit.app/ 
👉 Backend API: https://dropout-api.onrender.com

---

## 📌 Features
- Predicts student dropout risk
- User-friendly Streamlit interface
- Real-time API integration
- Logistic Regression ML model
- End-to-end deployment (Frontend + Backend)

---

## 🧠 Tech Stack
- Python
- Pandas, Scikit-learn
- Flask (Backend API)
- Streamlit (Frontend UI)
- Render (Backend Deployment)
- Streamlit Cloud (Frontend Deployment)
- GitHub (Version Control)

---

## 📂 Project Structure
```
student-dropout-predictor/
│
├── data/
│   └── student-data.csv
│
├── notebook/
│   └── model_training.ipynb
│
├── src/
│   ├── api.py
│   ├── model.pkl
│   └── logistic_regression.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
```

---

## ⚙️ How It Works
1. User inputs data (attendance, marks, etc.)
2. Streamlit sends request to Flask API
3. API loads trained ML model
4. Model predicts dropout risk
5. Result displayed on UI

---

## 📊 Model Details
- Algorithm: Logistic Regression
- Input Features:
  - Attendance
  - Marks
  - Backlogs
  - Study Hours
  - Stress Level

---

## 💡 Future Improvements
- Add more ML models (Random Forest, XGBoost)
- Improve UI design
- Add database integration
- Deploy using Docker & AWS

---

## 🙌 Author
Akansha Sharma
