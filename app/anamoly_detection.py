from datetime import datetime
from collections import defaultdict
from sklearn.ensemble import IsolationForest
import pandas as pd

def perform_anamoly_detection(data):
    # Extract date fields from the data
    subjects = data.get("subjects", [])
    exams = data.get("exams", [])
    study_plans = data.get("study_plans", [])
    events = data.get("events", [])

    date_counts = defaultdict(int)

    for subject in subjects:
        date = subject.get('date', '')  # Adjust based on actual data structure
        if date:
            date_counts[datetime.strptime(date, '%Y-%m-%d').date()] += 1

    for exam in exams:
        date = exam.get('date', '')  # Adjust based on actual data structure
        if date:
            date_counts[datetime.strptime(date, '%Y-%m-%d').date()] += 1

    for plan in study_plans:
        date = plan.get('dueDate', '')  # Adjust based on actual data structure
        if date:
            date_counts[datetime.strptime(date, '%Y-%m-%d').date()] += 1

    for event in events:
        date = event.get('date', '')  # Adjust based on actual data structure
        if date:
            date_counts[datetime.strptime(date, '%Y-%m-%d').date()] += 1

    # Prepare data for anomaly detection
    date_list = [{'date': date, 'count': count} for date, count in date_counts.items()]
    df = pd.DataFrame(date_list)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Use Isolation Forest for anomaly detection
    iso_forest = IsolationForest(contamination=0.1)
    df['anomaly'] = iso_forest.fit_predict(df[['count']])
    df['anomaly'] = df['anomaly'].apply(lambda x: x == -1)  # Mark anomalies

    # Prepare response
    anomaly_data = [{'date': date.strftime('%Y-%m-%d'), 'count': row['count'], 'anomaly': row['anomaly']}
                    for date, row in df.iterrows()]

    return anomaly_data
