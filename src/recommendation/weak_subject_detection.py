import pandas as pd

STREAM_SUBJECT_MAP = {
    "Science": ["maths", "physics", "chemistry", "biology", "english", "computer"],
    "Commerce": ["maths", "economics", "business studies", "accountancy", "english", "computer"],
    "Arts": ["Hindi", "english", "History", "Geography", "Political Science"]
}

CLASS_9_10_SUBJECTS = [
    "maths", "science","Social Science", "english", "computer"
]

ALL_SUBJECTS = [
    "maths", "english", "physics", "chemistry",
    "biology", "computer", "economics", "business studies", "accountancy", "Hindi", "History", "Geography", "Political Science", "science","Social Science"
]


def detect_weak_subjects(row):
    weak = []
    critical = []

    cls = row.get("class", None)
    stream = row.get("stream", None)

    # ✅ Class 9–10 → ignore commerce & arts
    if cls in [9, 10]:
        subject_cols = CLASS_9_10_SUBJECTS

    # ✅ Class 11–12 → filter by stream
    elif stream in STREAM_SUBJECT_MAP:
        subject_cols = STREAM_SUBJECT_MAP[stream]

    # ✅ Fallback
    else:
        subject_cols = ALL_SUBJECTS

    for sub in subject_cols:
        if sub in row and not pd.isna(row[sub]):
            if row[sub] < 40:
                critical.append(sub)
            elif row[sub] < 55:
                weak.append(sub)

    return weak, critical


def apply_weak_subject_detection(df):
    valid_cols = [col for col in ALL_SUBJECTS if col in df.columns]
    df["avg_marks"] = df[valid_cols].mean(axis=1) * 2

    df["weak_subjects"], df["critical_subjects"] = zip(
        *df.apply(detect_weak_subjects, axis=1)
    )

    return df