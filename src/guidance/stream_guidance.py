# Stream Guidance for Class 10
# Matches notebook logic exactly

def get_strength_subjects_10(marks):
    strengths = []
    for subject, score in marks.items():
        if score >= 60:
            strengths.append(subject)
    return strengths


def recommend_stream_class10(marks):
    strengths = get_strength_subjects_10(marks)

    has_maths = marks.get("Maths", 0) >= 60
    has_science = marks.get("Science", 0) >= 60
    has_computer = marks.get("Computer", 0) >= 60

    has_language = (
        marks.get("Hindi", 0) >= 60 or 
        marks.get("Social Science", 0) >= 60 or 
        marks.get("English", 0) >= 60
    )

    # 🔹 If Maths OR Science < 60 → Humanities
    if marks.get("Maths", 0) < 60 or marks.get("Science", 0) < 60:
        return (
            "Arts / Humanities",
            "Maths or Science below 60 — better suited for Humanities & Social Sciences"
        )

    # NON-MEDICAL (PCM)
    if has_maths and has_science:
        return (
            "Non-Medical (PCM)",
            "Strong in Maths & Science — suitable for Engineering & Technical fields"
        )

    # MEDICAL (PCB)
    elif has_science and not has_maths:
        return (
            "Medical (PCB)",
            "Strong in Science — suitable for Medical & Life Sciences"
        )

    # COMMERCE
    elif has_maths and not has_science:
        return (
            "Commerce",
            "Good in Maths — suitable for Business, Accounts & Finance"
        )

    # ARTS / HUMANITIES
    elif has_language:
        return (
            "Arts / Humanities",
            "Strong in Social Science & Languages — suitable for Law, Media, UPSC"
        )

    # FALLBACK
    else:
        return (
            "General / Skill-Based",
            "Focus on improving basics or exploring skill-based careers"
        )