#  Academic Decision Support System (ADSS)

**Major Project — Progress Up to Day 3**

##  Project Summary  

This project aims to develop an intelligent system that predicts student academic outcomes (**Pass/Fail**) and provides personalized academic, course, and career guidance based on performance, study habits, attendance, interests, and support systems.

The system uses:

- **Real-world student performance data** for machine learning prediction  
- **Synthetic student academic data** for guidance and recommendation modules  

---

##  Current Project Structure  
Academic_Decision_Support_System/
│
├── data/
│ ├── raw/
│ │ └── student-mat.csv # Real dataset
│ │
│ ├── synthetic/
│    └── student_academic_data.csv # Synthetic dataset
│ 
├── notebooks/
│ └── 01_data_exploration.ipynb
│
├── src/
├── models/
├── app/
├── reports/
└── generate_dataset.py

---

##  Datasets Used  

### 1️⃣ Real Dataset — Student Performance  

**File:** `student-mat.csv`  
**Source:** UCI Machine Learning Repository  
**Purpose:** Train Pass/Fail machine learning model  

**Key Attributes Used:**
- Study time  
- Absences  
- Family support  
- School support  
- Academic grades (G1, G2, G3)  

---

### 2️⃣ Synthetic Dataset — Student Academic Profiles  

**File:** `student_academic_data.csv`  
**Purpose:** Support guidance, recommendations, and career decisions  

**Includes:**
- Attendance patterns  
- Subject-wise marks  
- Interest areas  
- Activity involvement  
- Risk level classification  

---

##  Work Completed  

---

###  Day 1 — Project Setup & Dataset Preparation  

- Created structured project folders  
- Added real dataset for ML training  
- Generated synthetic student academic dataset  
- Organized datasets into appropriate folders  

---

###  Day 2 — Dataset Exploration & Understanding  

- Loaded and inspected real dataset  
- Checked dataset size, structure, and column types  
- Verified absence of missing values  
- Analyzed grade distributions  
- Studied impact of study time and absences on grades  
- Created Pass/Fail classification label  
- Identified key features for prediction  

---

###  Day 3 — Data Cleaning & Feature Preparation  

**Tasks Completed:**
- Reloaded real dataset for processing  
- Created binary Pass/Fail target variable based on final grade  
- Selected academically meaningful features:
  - Study time  
  - Absences  
  - Family support  
  - School support  
- Removed unrelated demographic attributes to reduce noise  
- Encoded categorical features into numeric values  
- Verified all model inputs are numeric  
- Created a cleaned and ML-ready dataset  

---

##  Key Outcomes from Day 3  

- Machine learning target column successfully created  
- Dataset transformed into numeric format  
- Only relevant educational features retained  
- Noise reduced for better prediction accuracy  
- Final dataset prepared for machine learning model training  

---

## 🎓 Academic Justification  

- Real dataset ensures **scientific credibility** in ML predictions  
- Synthetic dataset supports **privacy-safe guidance and recommendations**  
- Feature selection improves **model interpretability and performance**  
- Data preparation follows **industry-standard machine learning best practices**  

---

##  Next Step — Day 4 Plan  

➡ Train Pass/Fail Machine Learning Model  
➡ Evaluate prediction accuracy  
➡ Save trained model for reuse  

---

##  Project Status  

🟢 **Progressing — Data Ready for Model Training**

---

##  Author  

**Aman Kumar**  
B.Tech Computer Science Engineering  
Major Project — Academic Decision Support System  


