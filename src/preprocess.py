import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Encode target variable: Pass/Fail
    df["pass_fail"] = df["pass_fail"].map({
        "Fail": 0,
        "Pass": 1
    })

    # Label encode categorical columns
    label_cols = [
        "stress_level",
        "motivation_level",
        "family_support",
        "school_support",
        "activity_level"
    ]

    for col in label_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    return df