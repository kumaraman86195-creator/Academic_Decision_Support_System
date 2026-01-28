import numpy as np
import pandas as pd

np.random.seed(42)
n = 5000
data = []

for _ in range(n):
    cls = np.random.choice([9, 10, 11, 12])
    stream = "General"

    subjects = {
        "physics": np.nan,
        "chemistry": np.nan,
        "biology": np.nan,
        "maths": np.nan,
        "english": np.nan,
        "computer": np.nan,
        "commerce_sub": np.nan,
        "arts_sub": np.nan
    }

    # ---------------------------
    # SUBJECT ASSIGNMENT
    # ---------------------------
    if cls <= 10:
        subjects.update({
            "maths": np.random.randint(25, 100),
            "english": np.random.randint(25, 100),
            "computer": np.random.randint(25, 100),
            "physics": np.random.randint(25, 100),
            "chemistry": np.random.randint(25, 100)
        })
    else:
        stream = np.random.choice(["Medical", "Non-Medical", "Commerce", "Arts"])

        if stream == "Non-Medical":
            subjects.update({
                "physics": np.random.randint(25, 100),
                "chemistry": np.random.randint(25, 100),
                "maths": np.random.randint(25, 100),
                "english": np.random.randint(30, 100),
                "computer": np.random.randint(30, 100)
            })
        elif stream == "Medical":
            subjects.update({
                "physics": np.random.randint(25, 100),
                "chemistry": np.random.randint(25, 100),
                "biology": np.random.randint(25, 100),
                "english": np.random.randint(30, 100)
            })
        elif stream == "Commerce":
            subjects.update({
                "commerce_sub": np.random.randint(25, 100),
                "maths": np.random.randint(25, 100),
                "english": np.random.randint(30, 100),
                "computer": np.random.randint(30, 100)
            })
        else:  # Arts
            subjects.update({
                "arts_sub": np.random.randint(25, 100),
                "english": np.random.randint(30, 100)
            })

    # ---------------------------
    # BEHAVIOR FEATURES
    # ---------------------------
    previous_marks = np.random.randint(30, 100)
    study_hours = np.random.uniform(0.5, 6)
    absences = np.random.randint(0, 16)
    family_support = np.random.choice([0, 1], p=[0.35, 0.65])
    school_support = np.random.choice([0, 1], p=[0.4, 0.6])

    avg_marks = np.nanmean(list(subjects.values()))

    # ---------------------------
    # HARD FAIL FLOOR
    # ---------------------------
    if avg_marks < 35:
        pass_fail = 0

    else:
        # PRIMARY — current performance
        academic_score = avg_marks * 0.65
        
        # SECONDARY — previous academic record (STRONG)
        history_score = previous_marks * 0.45
        
        # TERTIARY — effort
        effort_score = study_hours * 3.0
        
        # LOW — attendance effect
        attendance_penalty = absences * 0.20
        
        # VERY LOW — support influence
        support_score = (family_support * 0.6) + (school_support * 0.4)
        
        # Noise
        noise = np.random.uniform(-7, 7)

        final_score = (
            academic_score +
            history_score +
            effort_score +
            support_score -
            attendance_penalty +
            noise
        )

        pass_fail = 1 if final_score >= 70 else 0

    row = {
        "class": cls,
        "stream": stream,
        "previous_marks": previous_marks,
        "study_hours": study_hours,
        "absences": absences,
        "family_support": family_support,
        "school_support": school_support,
        "pass_fail": pass_fail
    }

    row.update(subjects)
    data.append(row)


file_path = r"C:\Users\kumar\Academic_Decision_Support_System\data\synthetic\student_academic_data.csv"

df = pd.DataFrame(data)
df.to_csv(file_path, index=False)

print(f"File saved successfully at:\n{file_path}")
