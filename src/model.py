import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("data/student_dropout_data.csv")
data.columns = data.columns.str.strip()

X = data[['attendance','marks','backlogs','study_hours','stress_level']]
y = data['dropout_risk']

model = LogisticRegression(max_iter=500)
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully ✅")