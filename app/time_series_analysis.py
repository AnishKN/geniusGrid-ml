from datetime import datetime
from collections import defaultdict

# Sample data (replace with actual data from your database)
subjects = [
    {
        "_id": {"$oid": "667a54e4081906ad81d451b6"},
        "subName": "COMPUTER NETWORKS",
        "teacher": "NEHA",
        "color": "lime",
        "desc": "MODULE1-5",
        "status": "active",
        "__v": 0
    },
    {
        "_id": {"$oid": "667a561b081906ad81d451d0"},
        "subName": "DATA STRUCTURE",
        "teacher": "Raj",
        "color": "sky",
        "desc": "Modules 1 - 4",
        "status": "active",
        "__v": 0
    },
    # Add more subjects here
]

exams = [
    {
        "_id": {"$oid": "667a5525081906ad81d451be"},
        "subjectName": "COMPUTER NETWORKS",
        "examType": "Class Test",
        "date": "2024-06-29",
        "time": "02:00",
        "slot": "1",
        "room": "101",
        "status": "active",
        "__v": 0
    },
    {
        "_id": {"$oid": "667a563c081906ad81d451d8"},
        "subjectName": "DATA STRUCTURE",
        "examType": "Internal",
        "date": "2024-06-28",
        "time": "12:05",
        "slot": "2",
        "room": "102",
        "status": "active",
        "__v": 0
    },
    # Add more exams here
]

study_plans = [
    {
        "_id": {"$oid": "668eb6ba0ecd76aa43ea664e"},
        "title": "Math Study Plan",
        "desc": "Complete chapters 1 to 5",
        "dueDate": "2024-07-15",
        "dueTime": "14:00",
        "category": "Mathematics",
        "status": "Not Started",
        "progress": "0%",
        "studentId": {"$oid": "60d9f114f9a01b4a147c9a6e"},
        "__v": 0
    },
    # Add more study plans here
]

events = [
    {
        "_id": {"$oid": "6693dfcf70279a3643a8e55a"},
        "name": "Technical seminar",
        "type": "Seminar",
        "date": "2024-07-15",
        "time": "10:00",
        "venue": "AV Hall",
        "status": "active",
        "desc": "Prepare for Report and PPT",
        "__v": 0
    },
    # Add more events here
]

def perform_time_series_analysis():
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

    # Prepare response
    time_series_data = [{'date': date.strftime('%Y-%m-%d'), 'count': count} for date, count in date_counts.items()]

    return time_series_data
