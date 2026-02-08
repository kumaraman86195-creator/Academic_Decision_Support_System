feedback_map = {
    "maths": "Practice algebra and daily problem solving",
    "physics": "Revise formulas and practice numericals",
    "chemistry": "Revise reactions and NCERT concepts",
    "biology": "Focus on diagrams and concept clarity",
    "english": "Improve grammar, vocabulary, and reading",
    "computer": "Practice coding and logical thinking",
    "commerce_sub": "Revise accounting and financial basics",
    "arts_sub": "Improve theory understanding and writing"
}


def weak_subject_feedback(weak_list, critical_list):
    feedback = []

    for sub in critical_list:
        feedback.append(f"CRITICAL in {sub.upper()}: {feedback_map.get(sub)}")

    for sub in weak_list:
        feedback.append(f"Needs Improvement in {sub.upper()}: {feedback_map.get(sub)}")

    if not weak_list and not critical_list:
        feedback.append("No major weak subjects — Keep up the good work")

    return feedback


def apply_feedback(df):
    df["personalized_feedback"] = df.apply(
        lambda row: weak_subject_feedback(
            row["weak_subjects"],
            row["critical_subjects"]
        ),
        axis=1
    )
    return df