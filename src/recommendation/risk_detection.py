def subject_risk_level(row):
    score = 0

    score += len(row["critical_subjects"]) * 3
    score += len(row["weak_subjects"]) * 1

    if row["avg_marks"] < 45:
        score += 2

    if row["study_hours"] < 1.5:
        score += 1

    if score >= 6:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"

    return "Low Risk"


def apply_risk_detection(df):
    df["risk_level"] = df.apply(subject_risk_level, axis=1)
    return df