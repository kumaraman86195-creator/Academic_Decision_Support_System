from weak_subject_detection import detect_weak_areas, generate_weakness_feedback

import pandas as pd
df=pd.read_csv(r"C:\Users\kumar\Academic_Decision_Support_System\data\processed\student_performance_cleaned.csv")
sample = df.iloc[800]

weaknesses = detect_weak_areas(sample)
feedback = generate_weakness_feedback(weaknesses)

print("Weak Areas:", weaknesses)
print("\nFeedback:")
for i in feedback:
    print("-", i)