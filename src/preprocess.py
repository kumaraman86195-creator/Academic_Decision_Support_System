import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    subject_cols = [
        "physics", "chemistry", "maths", "biology",
        "english", "computer", "commerce_sub", "arts_sub"
    ]

    # Fill subject marks ONLY if they exist
    existing_subjects = [col for col in subject_cols if col in df.columns]
    if existing_subjects:
        df[existing_subjects] = df[existing_subjects].fillna(0)

        # Create avg_marks only if missing
        if "avg_marks" not in df.columns:
            df["avg_marks"] = df[existing_subjects].mean(axis=1) * 2

    # Encode target if exists
    if "pass_fail" in df.columns and df["pass_fail"].dtype == object:
        df["pass_fail"] = df["pass_fail"].str.lower().map({
            "fail": 0,
            "pass": 1
        })

    # Attendance score safe creation
    if "attendance_score" not in df.columns and "absences" in df.columns:
        df["attendance_score"] = 1 - (df["absences"] / 15)

    # Encode stream if exists
    if "stream" in df.columns:
        le = LabelEncoder()
        df["stream_encoded"] = le.fit_transform(df["stream"])

    # Convert supports safely
    for col in ["family_support", "school_support"]:
        if col in df.columns:
            df[col] = df[col].astype(int)

    return df