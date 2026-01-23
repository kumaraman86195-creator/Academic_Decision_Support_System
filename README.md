# Academic Decision Support System (ADSS)

## Project Overview
The Academic Decision Support System (ADSS) is designed to assist educators and students by predicting whether a student is likely to pass or fail based on academic and behavioral factors, and by providing actionable recommendations to improve academic performance and career direction.

This project aims to build an intelligent system that predicts student pass/fail outcomes and provides academic and career guidance based on study behavior, attendance, performance, interests, and support factors.

---

## System Uses

- Real student performance data for machine learning prediction  
- Synthetic student data for guidance, recommendations, and career decisions  

---

## Current Progress

✔ Project structure created  
✔ Real dataset collected  
✔ Synthetic dataset generated  
✔ Dataset organized into folders  
✔ Real dataset explored and analyzed  

---

## Project Structure (Current)

Academic_Decision_Support_System/
│
├── data/
│ ├── raw/
│ │ └── student-mat.csv   # Real dataset for ML
│ │
│ └── synthetic/
│ └── student_academic_data.csv # Generated synthetic dataset
│
├── notebooks/
│ └── 01_data_exploration.ipynb # Data exploration notebook
│
├── src/
├── models/
├── app/
├── reports/
└── generate_dataset.py # Synthetic dataset generator

---

## 📊 Datasets Used

### 1️⃣ Real Dataset — Student Performance (For ML Prediction)

**Source:** UCI Machine Learning Repository  
**File:** `student-mat.csv`  
**Purpose:** Train pass/fail prediction model  

**Key Features:**
- Study time  
- Absences  
- Family support  
- School support  
- Student grades (G1, G2, G3)  

📌 This dataset forms the backbone of the predictive model.

---

### 2️⃣ Synthetic Dataset — Student Academic Profile (For Guidance System)

**File:** `student_academic_data.csv`  
**Purpose:** Guidance and recommendation system  

**Includes:**
- Attendance  
- Study hours  
- Subject marks  
- Student interest areas  
- Family support level  
- Extracurricular involvement  
- Academic risk level  
- Stream and career guidance  

📌 Synthetic data is used to protect privacy while enabling realistic decision logic.

---

## 🛠️ Synthetic Dataset Generation

The script `generate_dataset.py` generates realistic synthetic student records including:

- Daily study hours  
- Attendance percentage  
- Subject-wise marks  
- Interest domains  
- Activity involvement  
- Academic risk level  

This dataset is used **only for guidance**, not ML training.

---

## 📅 Work Completed So Far

### ✅ Day 1 — Project Setup & Dataset Preparation
- Created project folder structure  
- Stored real dataset in `data/raw/`  
- Generated synthetic dataset using Python  
- Saved synthetic dataset in `data/synthetic/`  
- Ensured data files are reusable  

---

### ✅ Day 2 — Real Dataset Exploration & Understanding

**Tasks Performed:**
- Loaded real dataset into Python  
- Checked dataset shape and structure  
- Analyzed column data types  
- Verified missing values  
- Generated summary statistics  
- Created Pass/Fail target column  
- Analyzed:
  - Study time vs grades  
  - Absences vs performance  
  - Pass/Fail distribution  
- Identified key features for ML modeling  

---

## 📌 Key Insights from Day 2

- Dataset contains **395 student records**  
- No missing values found  
- Students who study more tend to score higher  
- Students with high absences tend to perform worse  
- Pass rate is higher than fail rate  

**Important prediction features identified:**
- Study time  
- Absences  
- Family support  
- School support  

---

## 🎯 Next Planned Step (Day 3)

➡ Data Cleaning  
➡ Feature Encoding  
➡ Feature Selection  
➡ Preparing dataset for Machine Learning  

---

## 🎓 Academic Justification

- Real dataset is used for predictive modeling to ensure credibility  
- Synthetic dataset is used for behavioral and career guidance due to privacy constraints  
- This ensures ethical, scientific, and academic validity  

---

## 📌 Author

**Aman Kumar**  
B.Tech CSE — Major Project  
Academic Decision Support System  

---

## 📌 Status

🟢 **Project in Progress — Day 2 Completed**
