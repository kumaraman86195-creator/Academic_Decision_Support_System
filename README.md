# 📘 Academic Decision Support System (ADSS)

### Major Project — Progress Up to Day 4  
**Project Type:** B.Tech CSE Final Year Major Project  

---

## 📌 Project Title  
**Intelligent Academic Performance Prediction and Guidance System**

---

## 📌 Project Objective  

To develop a **machine learning–based decision support system** that predicts **student pass/fail outcomes** using academic and behavioral data, and provides **data-driven academic improvement and career guidance**.

---

## 📁 Project Structure (Current)

Academic_Decision_Support_System/
│
├── data/
│ ├── raw/
│ │ └── student-mat.csv
│ ├── processed/
│ │ └── student_mat_cleaned.csv
│ └── synthetic/
│ └── student_academic_data.csv
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_feature_engineering.ipynb
│ └── 03_model_training.ipynb
│
├── models/
├── src/
├── app/
├── reports/
└── generate_dataset.py

---

# ✅ Work Completed So Far

---

## 🟢 Day 1 — Project Setup & Dataset Preparation  

- Created organized project folder structure  
- Stored real academic dataset (`student-mat.csv`)  
- Generated synthetic student academic dataset  
- Structured dataset folders for modular use  

---

## 🟢 Day 2 — Data Exploration & Understanding  

- Loaded and analyzed real dataset  
- Checked dataset shape, column types, and missing values  
- Generated descriptive statistics  
- Created **Pass/Fail target variable**  
- Studied relationships between:
  - Study time and grades  
  - Absences and performance  
- Analyzed **Pass/Fail distribution**  
- Identified key predictive features for ML modeling  

---

## 🟢 Day 3 — Data Cleaning & Feature Engineering  

- Selected meaningful predictive features:
  - Study time  
  - Absences  
  - Family support  
  - School support  
- Encoded categorical features  
- Removed irrelevant demographic attributes  
- Created a **cleaned ML-ready dataset**  

---

## 🟢 Day 4 — Machine Learning Model Training  

### 📌 Model Used  
**Random Forest Classifier**  
Chosen for its **robustness, high accuracy, resistance to overfitting, and interpretability**.

---

## 📊 Model Performance Results  

### ✅ Overall Model Accuracy  
Model Accuracy: 0.90 (90%)
This indicates **strong predictive performance** for student academic outcomes.

---

## 📋 Classification Report  

          precision    recall  f1-score   support

    Fail       0.88      0.81      0.85        27
    Pass       0.91      0.94      0.92        52

accuracy                           0.90        79

macro avg 0.89 0.88 0.89 79
weighted avg 0.90 0.90 0.90 79


### 🔍 Interpretation  

- The model performs **very well in predicting passing students**  
- High recall ensures **fewer incorrect pass predictions**  
- Balanced performance across both **Fail** and **Pass** classes  

---

## 📊 Confusion Matrix  

[[22 5]
[ 3 49]]


###  Meaning  

| Actual | Predicted Fail | Predicted Pass |
| ------ | -------------- | -------------- |
| Fail   | 22 Correct     | 5 Incorrect    |
| Pass   | 3 Incorrect    | 49 Correct     |

✔ Majority of predictions are correct  
✔ Low misclassification rate  
✔ Reliable classification behavior  

---

## 📈 Training vs Testing Accuracy  
Training Accuracy: 0.9937 (99.37%)
Testing Accuracy: 0.8987 (89.87%)

---

## 🔍 Underfitting / Overfitting Analysis  

- Training accuracy is **high**, indicating strong learning  
- Testing accuracy remains **high**, proving good generalization  
- The accuracy gap is **small (~9%)**, suggesting **minor overfitting**  

### 📌 Conclusion  

> The model **is not underfitting** (it has learned meaningful patterns).  
> The model shows **minor acceptable overfitting**, common in ensemble models.  
> Overall, the model **generalizes well to unseen student data**.

---

## 🎓 Academic Justification  

- Real student dataset ensures **scientific credibility**  
- Random Forest chosen for **stability, accuracy, and explainability**  
- Evaluation metrics include:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-Score  
  - Confusion Matrix  
- The system demonstrates **strong predictive reliability** for academic decision-making  

---

## 🎯 Next Planned Step — Day 5  

➡ Save trained ML model  
➡ Load model for real-time predictions  
➡ Build real-time student performance predictor  
➡ Begin deployment module  

---

## 📌 Project Status  

🟢 **Machine Learning Model Successfully Trained & Evaluated**  
🚧 **System Development In Progress**

---

## 📌 Author  

**Aman Kumar**  
B.Tech Computer Science & Engineering  
Final Year Major Project  
**Academic Decision Support System (ADSS)**  



