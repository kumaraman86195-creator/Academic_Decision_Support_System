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
| └── pass_fail_model.pkl
├── app/
├── reports/
| └── confusion_matrix.png
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

## 📊 Random Forest Model Performance Results  

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


## 🟢 Day 5 — Model Upgrade to XGBoost & Performance Re-Evaluation


### 📌 Model Updated
**XGBoost Classifier** (Extreme Gradient Boosting)


### 🔍 Why XGBoost Instead of Random Forest?


| Limitation in Random Forest |        Advantage of XGBoost       |
|-----------------------------|-----------------------------------|
| Feature importance not      | Better normalized feature         |
| normalized well             | importance                        |
| Less control over boosting  | Boosting improves weak learners   |
| Harder to tune for accuracy | Fine-grained hyperparameter tuning|
| Weaker handling of grade    | Better grade importance learning  |
|  feature weight             |                                   |

📌 **XGBoost was selected to improve accuracy, interpretability, and handling of grade-based prediction signals.**


---


## 📊 XGBoost Model Performance


### ✅ Overall Accuracy
     Model Accuracy: 0.96(96%)

📈 Performance improved compared to Random Forest.

---

## 📋 Classification Report  
       precision    recall  f1-score   support

           0       0.98      0.96      0.97       120
           1       0.94      0.97      0.96        80

    accuracy                           0.96       200
   macro avg       0.96      0.97      0.96       200
weighted avg       0.97      0.96      0.97       200


---

## 📊 Confusion Matrix  
    [[115   5]
    [ 2  78]]

### 🧠 Interpretation  

| Actual | Predicted Fail | Predicted Pass |
| ------ | -------------- | -------------- |
| Fail   | 115 Correct    | 5 Incorrect    |
| Pass   | 2 Incorrect    | 78 Correct     |

✔ Reduced misclassification  
✔ Improved recall for passing students  
✔ Strong generalization capability  

---

## 🖼 Confusion Matrix Visualization  

Saved as:  
reports/confusion_matrix.png


📌 This image visually represents model classification accuracy.

---

## 📈 Training vs Testing Accuracy  
     Training Accuracy: 1.0
     Testing Accuracy: 0.965

### 🔍 Overfitting Analysis  

- Training accuracy remains high  
- Testing accuracy is also strong  
- Performance gap is **small**, indicating **good generalization**  
- Model is **not underfitting** and shows **acceptable overfitting**

---

## 💾 Model Saved for Deployment  

Saved trained model file:
models/pass_fail_model.pkl


📌 The model can now be reused without retraining.

---

## 🧪 Model Tested on New Student Input  

The model was tested with **new unseen student data**, confirming:

✔ Accurate predictions  
✔ Stable output  
✔ Real-time prediction readiness  

📌 The model is now suitable for integration into a web or decision-support application.

---

## 🎓 Academic Justification  

- Real student dataset ensures **scientific credibility**  
- XGBoost selected for **superior accuracy, boosting capability, and feature importance normalization**  
- Evaluation metrics include:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-Score  
  - Confusion Matrix  
- The system demonstrates **strong predictive reliability** for academic decision-making  

---

## 🎯 Next Planned Step — Day 6  

➡ Generate performance and insight graphs
➡ Finalize ML model
➡ Results locked
➡ Ready for system integration
---

## 📌 Project Status  

🟢 **XGBoost Model Successfully Trained, Evaluated & Saved**  
🚧 **System Development In Progress**

---

## 📌 Author  

**Aman Kumar**  
B.Tech Computer Science & Engineering  
Final Year Major Project  
**Academic Decision Support System (ADSS)**  


