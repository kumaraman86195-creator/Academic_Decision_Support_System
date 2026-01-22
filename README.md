📘 Academic Decision Support System
📌 Project Overview

The Academic Decision Support System (ADSS) is designed to assist educators and students by predicting whether a student is likely to pass or fail based on academic and behavioral factors, and by providing actionable recommendations to improve academic performance.

The system combines:

Machine Learning (for prediction)

Rule-based logic (for guidance and decision support)

This repository currently documents Day 1: Project Setup & Dataset Preparation, which lays the foundation for future development.

🎯 Objectives – Day 1

The primary goals of Day 1 are:

Establish a clean and scalable project structure

Identify and organize datasets required for development

Understand and differentiate between real-world and synthetic datasets

Store datasets in reusable formats for future modeling and analysis

🗂️ Project Structure (Initial Setup)
Academic_Decision_Support_System/
│
├── data/
│   ├── raw/
│   │   └── student-mat.csv
│   │
│   └── synthetic/
│       └── student_academic_data.csv
│
├── generate_dataset.py
└── README.md

📊 Datasets Used
1️⃣ Real Dataset (For Machine Learning Prediction)

Source: UCI Machine Learning Repository

File: student-mat.csv

Purpose:

Used to train the Pass / Fail prediction model

Provides real-world credibility to the machine learning component

Key Attributes Include:

Study time

Absences

Family support

School support

Exam and internal assessment scores

📌 This dataset forms the backbone of the predictive model.

2️⃣ Synthetic Dataset (For Guidance & Decision Support)

File: student_academic_data.csv

Purpose:

Used for:

Academic risk analysis

Subject-wise improvement recommendations

Stream and career guidance

Key Attributes Include:

Family support level

Student interests

Extracurricular activity involvement

Academic risk level

📌 Synthetic data is generated to overcome privacy concerns and data availability limitations while still enabling realistic decision-support logic.

🛠️ Synthetic Dataset Generation

The script generate_dataset.py is responsible for generating a realistic synthetic dataset and storing it locally in CSV format.

Features Generated:

Daily study hours

Attendance percentage

Subject-wise marks

Interest domains

Activity involvement

Academic risk level

Rule-based predicted pass/fail status

The generated dataset is reusable across multiple modules such as analysis, recommendations, and visualization.

🧪 Tools & Technologies (Day 1)

Python 3

Pandas

NumPy

✅ Day 1 Outcomes

✔ Clean and organized project folder structure created
✔ Real-world dataset identified and stored securely
✔ Synthetic dataset generated and saved for reuse
✔ Clear separation between prediction data and guidance data
✔ Strong foundation established for future development

🚧 Project Status

Under active development

Future phases will include:

Machine learning model training

Recommendation engine

Visualization and deployment