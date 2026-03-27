# 📊 Codveda Internship — Intermediate Level Tasks  
### 🚀 Applied Machine Learning: Regression & Classification (Real Metrics Included)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Level](https://img.shields.io/badge/Level-Intermediate-orange)
![ML](https://img.shields.io/badge/Machine%20Learning-Applied-brightgreen)

---

## 📌 Overview  

This repository contains my **Intermediate Level Machine Learning tasks** completed during my internship at <b>Codveda Technology</b>.  

At this stage, I applied **supervised learning techniques** to solve two real-world problems:

- 🏠 **House Price Prediction (Regression)**  
- 📉 **Customer Churn Prediction (Classification)**  

The focus was on **model building, evaluation, and performance optimization** using real datasets.

---

## 🔄 Workflow  

```
Data → Cleaning → Feature Engineering → Model Training → Evaluation → Optimization
```

---

## 📂 Project Structure  

```
COdveda_Tech_Intern_Intermidiate_Level_Task/
│
├── Regression(House_Dataset)_Task1.ipynb
├── house Prediction Data Set.csv
│
├── Classification with Logistic Regression(Task2).ipynb
├── Churn Prediction Data/
│
└── README.md
```

---

## 🛠️ Tech Stack  

- Python (Pandas, NumPy)  
- Matplotlib, Seaborn  
- Scikit-learn  
- Logistic Regression  
- Decision Tree  
- Random Forest  

---

# 🔍 Project Breakdown  

---

## 🏠 1️⃣ House Price Prediction (Regression)

### 🎯 Objective  
Predict housing prices based on multiple economic and structural features.

---

### 🤖 Models Implemented  

| Model              | MSE       | R² Score |
|-------------------|----------|---------|
| Linear Regression | 24.29     | 0.67    |
| Decision Tree     | 10.42     | 0.86    |
| Random Forest     | **7.90**  | **0.89** |

---

### 📊 Key Insights  

- ✅ **Random Forest performed best** with R² = **0.89**, capturing complex relationships  
- 📉 Linear Regression showed moderate performance → indicates partial linear relationships  
- 🌳 Decision Tree improved accuracy but may overfit  
- 🌲 Ensemble models (Random Forest) provided **most reliable predictions**

---

### 💡 Interpretation  

- Housing prices depend on **non-linear feature interactions**  
- Advanced models significantly outperform basic linear approaches  

---

## 📉 2️⃣ Customer Churn Prediction (Classification)

### 🎯 Objective  
Predict whether a customer is likely to churn.

---

## 🔹 Baseline Model (Logistic Regression)

- **Accuracy:** 86%  
- **Precision:** 61%  
- **Recall:** 22%  

### ⚠️ Insight  
- High accuracy but **very low recall** → model misses many churn customers  
- Indicates **class imbalance problem**

---

## 🔹 Improved Model (Balanced + Scaled Logistic Regression)

- **Accuracy:** 76%  
- **Precision (Churn):** 35%  
- **Recall (Churn):** **71%**  
- **F1 Score (Churn):** 0.47  

---

### 📊 Key Improvements  

- Recall improved from **22% → 71%** 🚀  
- Model now detects **majority of churn customers**  
- Trade-off: lower precision (more false positives)

---

### 📈 Model Comparison Insight  

| Metric   | Before Fix | After Fix |
|----------|-----------|----------|
| Accuracy | 86%       | 76%      |
| Recall   | 22%       | **71%**  |
| Precision| 61%       | 35%      |

---

### 💡 Business Interpretation  

- 📉 Missing churn customers = **revenue loss**  
- Improved model prioritizes **recall over accuracy**  
- Better for **real-world retention strategies**

---

## 📊 ROC Curve Insight  

- Model shows ability to distinguish churn vs non-churn  
- Used AUC metric to evaluate classification performance  

---

## 📊 Key Takeaways Across Projects  

✔ Feature engineering and preprocessing significantly impact results  
✔ Model selection determines predictive performance  
✔ Ensemble models outperform simpler models  
✔ Handling class imbalance is critical in classification problems  

---

## 💡 Business Value  

- 🏠 Enables accurate **real estate price prediction**  
- 📉 Helps businesses **identify and retain at-risk customers**  
- 📊 Supports **data-driven decision making and forecasting**  

---

## 🧩 Challenges & Solutions  

| Challenge | Solution |
|----------|---------|
| Class imbalance | Applied `class_weight='balanced'` |
| Model convergence | Increased iterations + scaling |
| Non-linear data | Used Random Forest |
| Low recall | Optimized model for better detection |

---

## 🚀 How to Run  

```bash
git clone https://github.com/HamzyinTech/Codvede_Technology_Intern_Project.git

cd Codvede_Technology_Intern_Project/Codveda_Tech_Intern_Intermidiate_Level_Task

pip install -r requirements.txt

jupyter notebook
```

---

## 🏆 Key Achievements  

✔ Built and compared multiple ML models  
✔ Improved churn detection by **+49% recall increase**  
✔ Achieved **~89% explanatory power (R²) in regression**  
✔ Applied real-world ML optimization techniques  

---

## 👨‍💻 Author  

**Oyegoke Hamad**  
- Data Scientist | Data Analyst  
- Focused on solving real-world problems with data  

---

## ⭐ Support  

If you found this project useful:

- ⭐ Star the repository  
- 🍴 Fork it  
- 📢 Share with others  

---
