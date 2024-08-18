import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np

def perform_generate_study_plan(data):
    # Extract data from the request
    subjects = data.get("subjects", [])
    study_plans = data.get("study_plans", [])
    exams = data.get("exams", [])
    events = data.get("events", [])
    students = data.get("students", [])

    # Check if there is enough data to proceed
    if not subjects or not study_plans or not exams or not events or not students:
        return {"error": "Insufficient data to generate study plans"}

    # Prepare the data for the machine learning model
    study_plan_data = []
    for plan in study_plans:
        study_plan_data.append({
            "student_id": plan.get("studentId", {}).get("$oid", ""),
            "title": plan.get("title", ""),
            "due_date": plan.get("dueDate", ""),
            "progress": int(plan.get("progress", "0").replace('%', ''))
        })

    exam_data = []
    for exam in exams:
        exam_data.append({
            "subject_name": exam.get("subjectName", ""),
            "exam_type": exam.get("examType", ""),
            "date": exam.get("date", "")
        })

    event_data = []
    for event in events:
        event_data.append({
            "event_name": event.get("name", ""),
            "event_type": event.get("type", ""),
            "date": event.get("date", "")
        })

    # Convert to DataFrame
    df_study_plans = pd.DataFrame(study_plan_data)
    df_exams = pd.DataFrame(exam_data)
    df_events = pd.DataFrame(event_data)

    # Feature Engineering
    # Assuming the columns: student_id, title, due_date, progress
    df_study_plans['due_date'] = pd.to_datetime(df_study_plans['due_date'])
    df_study_plans['days_until_due'] = (df_study_plans['due_date'] - pd.Timestamp.now()).dt.days

    # We need to convert categorical data to numerical data for the model
    df_study_plans = pd.get_dummies(df_study_plans, columns=['title'])

    # For simplicity, let's assume 'progress' is the target variable
    X = df_study_plans.drop(columns=['student_id', 'due_date', 'progress'])
    y = df_study_plans['progress']

    # Train a simple Decision Tree Regressor model
    model = DecisionTreeRegressor()
    model.fit(X, y)

    # Predict study plans for the next period
    future_study_plans = []
    for student in students:
        student_id = student.get("_id", {}).get("$oid", "")
        # Assuming we need to predict for a new study plan
        new_plan_features = {
            "days_until_due": 7  # Example: predict for a plan due in 7 days
        }
        new_plan_features = pd.DataFrame([new_plan_features])
        new_plan_features = pd.get_dummies(new_plan_features)

        # Align new_plan_features columns with the training data
        new_plan_features = new_plan_features.reindex(columns=X.columns, fill_value=0)

        predicted_progress = model.predict(new_plan_features)[0]

        future_study_plans.append({
            "student_id": student_id,
            "predicted_progress": predicted_progress
        })

    return {"study_plans": future_study_plans}
