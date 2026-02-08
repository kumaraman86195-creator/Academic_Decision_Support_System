import pandas as pd
from pipeline import run_recommendation_pipeline

test_student = {
    "class": 12,
    "stream": "Non Medical",
    "physics": 80,
    "chemistry": 65,
    "maths": 67,
    "english": 53,
    "computer": 33,
    "biology": None,
    "commerce_sub": None,
    "arts_sub": None,
    "study_hours": 5
}

# Convert to DataFrame
sample = pd.DataFrame([test_student])

# Run pipeline
sample = run_recommendation_pipeline(sample)

row = sample.iloc[0]

print("\n--- TEST STUDENT RESULT ---")
print("Class:", row["class"])
print("Stream:", row["stream"])
print("Weak Subjects:", row["weak_subjects"])
print("Critical Subjects:", row["critical_subjects"])
print("Risk Level:", row["risk_level"])

print("\nFeedback:")
for f in row["personalized_feedback"]:
    print("-", f)

print("\nRecommended Courses:")
for subject, courses in row["recommended_courses"].items():
    print(f"- {subject.upper()}: {', '.join(courses)}")