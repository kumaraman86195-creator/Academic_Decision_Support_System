def detect_weak_areas(student_row):
    """
    Detect weak academic and behavioral areas for a student.
    Returns a list of weakness labels.
    """

    weak_areas = []

    # Academic Performance
    if student_row["avg_grade"] < 60:
        weak_areas.append("Low Academic Performance")

    # Attendance Issues
    if student_row["attendance_percentage"] < 75:
        weak_areas.append("Poor Attendance")

    if student_row["absences"] > 10:
        weak_areas.append("High Absences")

    # Study Habits
    if student_row["study_hours_per_day"] < 2:
        weak_areas.append("Low Study Time")

    # Mental & Motivation Factors
    if student_row["stress_level"] >= 3:
        weak_areas.append("High Stress")

    if student_row["motivation_level"] <= 1:
        weak_areas.append("Low Motivation")

    # If no weakness found
    if not weak_areas:
        weak_areas.append("No Major Weakness Detected")

    return weak_areas


def generate_weakness_feedback(weak_list):
    """
    Generate personalized improvement feedback based on weak areas.
    """

    feedback_map = {
        "Low Academic Performance": "Revise weak subjects regularly and practice more problem-solving questions.",
        "Poor Attendance": "Improve class attendance to avoid missing important academic concepts.",
        "High Absences": "Reduce absences and maintain consistent classroom participation.",
        "Low Study Time": "Increase daily study hours and follow a structured study routine.",
        "High Stress": "Practice stress management techniques like breaks, exercise, and mindfulness.",
        "Low Motivation": "Set achievable goals and track progress to stay motivated.",
        "No Major Weakness Detected": "Great job! Continue maintaining your strong academic habits."
    }

    feedback = []

    for weakness in weak_list:
        if weakness in feedback_map:
            feedback.append(feedback_map[weakness])
        else:
            feedback.append(f"Work on improving: {weakness}")

    return feedback