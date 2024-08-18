def generate_recommendations(data):
    recommendations = []
    for student in data:
        student_recommendations = {
            "email": student["email"],
            "prioritySubjects": sorted(student["preferredSubjects"], key=lambda x: x["priority"]),
            "learningMaterials": "Videos" if student["learningStyle"] == "Visual" else "Podcasts" if student["learningStyle"] == "Auditory" else "Hands-on Practice"
        }
        recommendations.append(student_recommendations)
    return recommendations
