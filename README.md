# Academic Decision Support System



# Project Overview

This project aims to build an intelligent system that predicts student pass/fail outcomes and provides academic and career guidance based on study behavior, attendance, performance, interests, and support factors.

The system uses:

Real student performance data for machine learning prediction

Synthetic student data for guidance, recommendations, and career decisions

# Current Progress

✔ Project structure created
✔ Real dataset collected
✔ Synthetic dataset generated
✔ Dataset organized into folders
✔ Real dataset explored and analyzed

# Project Structure (Current)
Academic_Decision_Support_System/
│
├── data/
│   ├── raw/
│   │   └── student-mat.csv              # Real dataset for ML
│   │
│   └── synthetic/
│       └── student_academic_data.csv    # Generated synthetic dataset
│
├── notebooks/
│   └── 01_data_exploration.ipynb        # Data exploration notebook
│
├── src/
├── models/
├── app/
├── reports/
└── generate_dataset.py                  # Synthetic dataset generator

# Datasets Used
1️⃣ Real Dataset — Student Performance

File: student-mat.csv
Purpose: Train pass/fail prediction model
Key Features:

Study time

Absences

Family support

School support

Student grades (G1, G2, G3)

This dataset is used to build the core machine learning model.

2️⃣ Synthetic Dataset — Student Academic Profile

File: student_academic_data.csv
Purpose: Guidance and recommendation system
Includes:

Attendance

Study hours

Subject marks

Interest areas

Activity involvement

Risk level

This dataset is used for decision-support logic, not ML training.

📅 Work Completed So Far
✅ Day 1 — Project Setup & Dataset Preparation

Created project folder structure

Stored real dataset in data/raw/

Generated synthetic dataset using Python

Saved synthetic dataset in data/synthetic/

Ensured data files are reusable

✅ Day 2 — Real Dataset Exploration & Understanding
Tasks Performed:

Loaded real dataset into Python

Checked dataset shape and structure

Analyzed column data types

Verified missing values

Generated summary statistics

Created Pass/Fail target column

Analyzed:

Study time vs grades

Absences vs performance

Pass/Fail distribution

Identified key features for ML modeling

# Key Insights from Day 2

Dataset contains 395 student records

No missing values found

Students who study more tend to score higher

Students with high absences tend to perform worse

Pass rate is higher than fail rate

Important prediction features identified:

Study time

Absences

Family support

School support

🎯 Next Planned Step (Day 3)

➡ Data Cleaning
➡ Feature Encoding
➡ Feature Selection
➡ Preparing dataset for Machine Learning

🎓 Academic Justification

Real dataset is used for predictive modeling to ensure credibility

Synthetic dataset is used for behavioral and career guidance because real personal data is not publicly available

This separation maintains ethical, scientific, and academic validity

📌 Author
Aman Kumar
B.Tech CSE — Major Project
Academic Decision Support System

📌 Status

🟢 Project in Progress — Day 2 Completed