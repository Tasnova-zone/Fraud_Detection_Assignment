💳 Credit Card Fraud Detection – Machine Learning Project
A comprehensive end-to-end machine learning project focused on identifying fraudulent credit card transactions using the Kaggle Credit Card Fraud Dataset.
Conducted as part of a 2-week industrial attachment at Brain Station 23, this project covers the full ML pipeline — from data exploration to deploying a web-based prediction tool.

📁 Dataset Overview
Source: Kaggle – Credit Card Fraud Detection Dataset

File Format: CSV (creditcard.csv)

Total Transactions: 284,807

Features: 30

28 anonymized principal components (V1–V28)

Time, Amount

Target Variable:

Class: 1 = Fraud, 0 = Normal

Class imbalance: Fraud cases ~0.17%

📅 Project Timeline & Key Milestones
Day	Focus Area
Day 1	Python Basics & Financial Data Exploration
Day 2	EDA & Visualization
Day 3	Model Training & Evaluation
Day 4	Feature Engineering & Model Tuning
Day 5	Streamlit App Development & Deployment

🔎 Day 2 – Exploratory Data Analysis (EDA)
✅ Actions:
Loaded and inspected the dataset using Pandas

Verified data integrity (null checks, data types)

Identified severe class imbalance

Created visualizations:

Class distribution bar chart

Histograms & KDE plots

Boxplots for outlier detection

Correlation heatmaps

Log-scaled fraud vs. amount distribution

📌 Key Findings:
Fraudulent cases ≈ 0.17% of total data

Top fraud indicators: V14, V12, V17

Fraud transactions typically involve lower amounts

Time showed no significant correlation with fraud

🤖 Day 3 – Initial Model Building & Evaluation
📌 Models Trained:
Logistic Regression

Decision Tree

K-Nearest Neighbors (KNN)

Naive Bayes

🧪 Evaluation Metrics:
Model	Accuracy	Precision	Recall	F1 Score	ROC AUC
Naive Bayes	0.976	0.059	0.847	0.087	0.963
Logistic Regression	0.999	0.829	0.643	0.723	0.957
KNN	0.999	0.919	0.806	0.858	0.944
Decision Tree	0.999	0.895	0.786	0.837	0.901

🔍 Observations:
Logistic Regression: High precision but lower recall

Naive Bayes: Best recall, but many false positives

KNN & Decision Tree: More balanced performance

🛠️ Day 4 – Feature Engineering & Model Tuning
🔧 Preprocessing Steps:
Normalized Time and Amount with StandardScaler

Balanced data using:

Undersampling

class_weight='balanced'

Hyperparameter tuning using GridSearchCV

✅ Tuned Models:
Random Forest

Gradient Boosting

Decision Tree (as baseline)

📈 Final Evaluation Results:
Model	ROC AUC	F1 Score	Precision	Recall
Random Forest	0.983	0.933	0.992	0.880
Gradient Boosting	0.982	0.927	0.971	0.887
Decision Tree	0.933	0.912	0.970	0.860

🧠 Best Hyperparameters (Random Forest):
python
Copy code
{'n_estimators': 200, 'max_depth': 20, 'min_samples_split': 2}
🌐 Day 5 – Streamlit App Deployment
🎯 Objective:
Develop a simple web interface that allows users to input transaction details and get fraud prediction results using the trained Random Forest model.

🛠️ Tech Stack:
Frontend: Streamlit (Python)

Model Serving: Random Forest serialized with joblib

🖥️ How to Use:
Save fraud_model.pkl (trained model) and app.py in the same folder

Run the app using:

bash
Copy code
streamlit run app.py
Enter transaction details in the form

The app returns a fraud probability and classification result

✅ Final Summary
This project demonstrates the complete end-to-end process of building a machine learning solution for fraud detection:

Data Exploration: Understanding imbalance and key features

Model Training: Baseline + advanced models

Feature Engineering: Scaling, balancing, tuning

Evaluation: ROC AUC, F1 Score, Precision, Recall

Deployment: Streamlit web app for real-time inference

📌 Key Achievements:
Achieved high accuracy and recall using ensemble methods

Identified fraud-indicative features

Built and deployed a usable web prediction tool

Gained hands-on experience in both ML and full-stack deployment
