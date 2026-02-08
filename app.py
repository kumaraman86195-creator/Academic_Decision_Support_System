import streamlit as st
import pandas as pd

from src.predict import predict_student
from src.recommendation.pipeline import run_recommendation_pipeline
from src.guidance.stream_guidance import recommend_stream_class10
from src.guidance.career_guidance import recommend_career_class12

st.set_page_config(page_title="ADSS", layout="wide")

st.title("🎓 Academic Decision Support System (ADSS)")

menu = st.sidebar.radio(
    "Choose Module",
    ["Pass/Fail Prediction", "Academic Recommendation", "Stream & Career Guidance"]
)

# =====================================================
# 1️⃣ PASS / FAIL PREDICTION
# =====================================================
if menu == "Pass/Fail Prediction":

    st.header("📊 Pass / Fail Prediction")

    col1, col2 = st.columns(2)

    with col1:
        avg_marks = st.number_input("Average Marks", 0, 100, 65)
        previous_marks = st.number_input("Previous Marks", 0, 100, 60)
        study_hours = st.number_input("Study Hours", 0.0, 10.0, 2.5)

    with col2:
        absences = st.number_input("Absences", 0, 20, 3)
        family_support = st.selectbox("Family Support", [0, 1])
        school_support = st.selectbox("School Support", [0, 1])

    if st.button("Predict Result"):
        input_data = {
            "avg_marks": avg_marks,
            "previous_marks": previous_marks,
            "study_hours": study_hours,
            "attendance_score": 1 - (absences / 15),
            "family_support": family_support,
            "school_support": school_support
        }

        prediction, probability = predict_student(input_data)

        if prediction == 1:
            st.success(f"✅ PASS — Confidence: {probability:.2f}")
        else:
            st.error(f"❌ FAIL — Confidence: {probability:.2f}")

# =====================================================
# 2️⃣ ACADEMIC RECOMMENDATION
# =====================================================
elif menu == "Academic Recommendation":

    st.header("📘 Academic Recommendation")

    cls = st.selectbox("Class", [9, 10, 11, 12])

    # Stream logic
    if cls <= 10:
        stream = "Not Required"
        st.info("Stream not required for Class 9–10")
    else:
        stream = st.selectbox("Stream", ["Science", "Commerce", "Arts"])

    student = {"class": cls, "stream": stream}

    # --------------------------
    # CLASS 9–10 SUBJECT INPUT
    # --------------------------
    if cls <= 10:
        student.update({
            "maths": st.number_input("Maths", 0, 100, 60),
            "science": st.number_input("Science", 0, 100, 55),
            "Social Science": st.number_input("Social Science", 0, 100, 58),
            "english": st.number_input("English", 0, 100, 65),
            "computer": st.number_input("Computer", 0, 100, 70),
        })

    # --------------------------
    # CLASS 11–12 SCIENCE
    # --------------------------
    elif stream == "Science":
        student.update({
            "maths": st.number_input("Maths", 0, 100, 60),
            "physics": st.number_input("Physics", 0, 100, 55),
            "chemistry": st.number_input("Chemistry", 0, 100, 50),
            "biology": st.number_input("Biology", 0, 100, 45),
            "english": st.number_input("English", 0, 100, 65),
            "computer": st.number_input("Computer", 0, 100, 70),
        })

    # --------------------------
    # CLASS 11–12 COMMERCE
    # --------------------------
    elif stream == "Commerce":
        student.update({
            "maths": st.number_input("Maths", 0, 100, 60),
            "economics": st.number_input("Economics", 0, 100, 55),
            "business studies": st.number_input("Business Studies", 0, 100, 50),
            "accountancy": st.number_input("Accountancy", 0, 100, 45),
            "english": st.number_input("English", 0, 100, 65),
            "computer": st.number_input("Computer", 0, 100, 70),
        })

    # --------------------------
    # CLASS 11–12 ARTS
    # --------------------------
    elif stream == "Arts":
        student.update({
            "Hindi": st.number_input("Hindi", 0, 100, 60),
            "History": st.number_input("History", 0, 100, 55),
            "Geography": st.number_input("Geography", 0, 100, 50),
            "Political Science": st.number_input("Political Science", 0, 100, 45),
            "english": st.number_input("English", 0, 100, 65),
        })

    # Study hours (common)
    student["study_hours"] = st.number_input("Study Hours", 0.0, 10.0, 2.0)

    if st.button("Generate Recommendation"):
        df = pd.DataFrame([student])
        result = run_recommendation_pipeline(df)
        row = result.iloc[0]

        st.subheader("📉 Weak Subjects")
        st.write(row["weak_subjects"])

        st.subheader("🚨 Critical Subjects")
        st.write(row["critical_subjects"])

        st.subheader("⚠ Risk Level")
        st.warning(row["risk_level"])

        st.subheader("📝 Personalized Feedback")
        for f in row["personalized_feedback"]:
            st.info(f)

        st.subheader("📚 Course Recommendations")
        for subject, courses in row["recommended_courses"].items():
            st.write(f"**{subject.upper()}** → {', '.join(courses)}")

# =====================================================
# 3️⃣ STREAM & CAREER GUIDANCE
# =====================================================
elif menu == "Stream & Career Guidance":

    st.header("🎯 Guidance")

    tab1, tab2 = st.tabs(["Class 10 Stream Guidance", "Class 12 Career Guidance"])

    # -------- CLASS 10 --------
    with tab1:
        st.subheader("Class 10 Stream Recommendation")

        marks = {
            "Maths": st.number_input("Maths", 0, 100, 65, key="m1"),
            "Science": st.number_input("Science", 0, 100, 62, key="m2"),
            "Computer": st.number_input("Computer", 0, 100, 70, key="m3"),
            "Hindi": st.number_input("Hindi", 0, 100, 55, key="m4"),
            "Social Science": st.number_input("Social Science", 0, 100, 58, key="m5")
        }

        if st.button("Recommend Stream"):
            stream, reason = recommend_stream_class10(marks)
            st.success(f"🎓 Recommended Stream: {stream}")
            st.info(reason)

    # -------- CLASS 12 --------
    with tab2:
        st.subheader("Class 12 Career Recommendation")

        stream = st.selectbox("Stream", ["Non-Medical", "Medical", "Commerce", "Arts"])
        avg_500 = st.number_input("Marks Out of 500", 0, 500, 320)
        activity_score = st.slider("Activity Score", 0, 10, 5)

        if st.button("Recommend Career"):
            careers, colleges, advice = recommend_career_class12(stream, avg_500, activity_score)

            st.subheader("💼 Career Options")
            st.write(careers)

            st.subheader("🏫 Colleges")
            st.write(colleges)

            st.subheader("📌 Advice")
            for tip in advice:
                st.info(tip)