import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 100500

data = {
    "student_id": range(1, n + 1),
    "grade_level": np.random.randint(6, 13, n),
    "study_hours_per_day": np.round(np.random.uniform(0.5, 6, n), 1),
    "attendance_percentage": np.random.randint(60, 100, n),
    "absences": np.random.randint(0, 30, n),
    "family_support_level": np.random.choice(
        ["Low", "Medium", "High"], n, p=[0.25, 0.45, 0.30]
    ),
    "school_support_level": np.random.choice(
        ["Low", "Medium", "High"], n, p=[0.30, 0.45, 0.25]
    ),
    "math_marks": np.random.randint(30, 100, n),
    "science_marks": np.random.randint(30, 100, n),
    "english_marks": np.random.randint(30, 100, n),
    "interest_area": np.random.choice(
        ["Science", "Commerce", "Arts", "Sports"], n
    ),
    "activity_involvement": np.random.choice(
        ["Yes", "No"], n, p=[0.55, 0.45]
    ),
    "activity_performance_level": np.random.choice(
        ["Low", "Medium", "High"], n, p=[0.3, 0.4, 0.3]
    )
}

df = pd.DataFrame(data)

df["overall_percentage"] = (
    df["math_marks"] + df["science_marks"] + df["english_marks"]
) / 3

df["predicted_result"] = np.where(
    (df["overall_percentage"] >= 40) & (df["attendance_percentage"] >= 75),
    "Pass",
    "Fail"
)

df["risk_level"] = pd.cut(
    df["overall_percentage"],
    bins=[0, 40, 60, 100],
    labels=["High", "Medium", "Low"]
)

# 🔽 CHANGE THIS PATH
file_path = r"C:\Users\kumar\Academic_Decision_Support_System\data\synthetic\student_academic_data.csv"

df.to_csv(file_path, index=False)

print(f"File saved successfully at:\n{file_path}")
