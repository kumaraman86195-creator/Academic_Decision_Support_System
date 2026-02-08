course_map_9_10 = {
    "maths": [
        "CBSE Mathematics Class 9–10 (PW)",
        "PW Foundation Maths Course",
        "Vedantu Maths for Class 9–10"
    ],
    
    "science": [
        "CBSE Science Class 9–10 (PW)",
        "PW Science Foundation Course",
        "Byju’s Science Course for Class 9–10"
    ],
    
    "social science": [
        "CBSE Social Science Class 9–10 (PW)",
        "Vedantu SST Foundation Course",
        "Byju’s Social Science Course"
    ],
    
    "english": [
        "PW English Grammar & Writing",
        "Spoken English Course (Indian Context)",
        "Vedantu English for CBSE"
    ],
    
    "computer": [
        "Basic Computer Course (Class 9–10)",
        "PW Python for Beginners",
        "Coding for Kids (India)"
    ]
}


course_map_11_12 = {
    "maths": [
        "CBSE Mathematics Class 11–12 (PW)",
        "PW JEE Maths Foundation",
        "Unacademy Class 11–12 Maths"
    ],
    "physics": [
        "CBSE Physics Class 11–12 (PW)",
        "PW JEE Physics Foundation",
        "Vedantu Physics Course"
    ],
    "chemistry": [
        "CBSE Chemistry Class 11–12 (PW)",
        "PW NEET/JEE Chemistry Foundation",
        "Unacademy Chemistry Course"
    ],
    "biology": [
        "CBSE Biology Class 11–12 (PW)",
        "PW NEET Biology Foundation",
        "Byju’s Biology for NEET"
    ],
    "english": [
        "CBSE English Core Class 11–12",
        "PW English Writing & Literature",
        "Spoken English & Communication"
    ],
    "computer": [
        "CBSE Computer Science / IP",
        "PW Python & SQL Basics",
        "Basic Data Structures for Beginners"
    ],
    "accountancy": [
        "CBSE Accountancy Class 11–12",
        "PW Commerce Foundation Course",
        "CA Foundation Basics (PW)"
    ],
    "business studies": [
        "CBSE Business Studies Class 11–12",
        "PW Business Studies Course"
    ],
    "economics": [
        "CBSE Economics Class 11–12",
        "PW Economics Foundation"
    ],
    "political science": [
        "CBSE Political Science Class 11–12",
        "PW Humanities Course"
    ],
    "history": [
        "CBSE History Class 11–12"
    ],
    "geography": [
        "CBSE Geography Class 11–12"
    ],
    "hindi": [
        "CBSE Hindi Core Class 11–12"
    ]
}

def recommend_courses(row):
    cls = row["class"]
    weak_subjects = row["weak_subjects"] + row["critical_subjects"]
    stream = row.get("stream", None)

    # Filter courses by stream relevance
    if stream == "Arts":
        weak_subjects = [s for s in weak_subjects if s in ["history", "geography", "political science", "english"]]
    elif stream == "Commerce":
        weak_subjects = [s for s in weak_subjects if s in ["accountancy", "business studies", "economics", "maths", "english"]]

    course_map = course_map_9_10 if cls <= 10 else course_map_11_12

    recommendations = {}

    for subject in weak_subjects:
        courses = course_map.get(subject, [])
        if courses:
            recommendations[subject] = courses

    if not recommendations:
        recommendations["general"] = ["Maintain Performance Program"]

    return recommendations


def apply_course_recommendation(df):
    df["recommended_courses"] = df.apply(recommend_courses, axis=1)
    return df