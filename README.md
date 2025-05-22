💳 Credit Card Fraud Detection – Machine Learning Project
A comprehensive project focused on identifying fraudulent transactions using the Credit Card Fraud Detection Dataset from Kaggle. This 2-week industrial attachment project at Brain Station 23 followed a full ML pipeline: from data exploration to advanced model tuning.

📅 Project Timeline & Key Milestones
Day	Focus Area
Day 2	Data Analysis & Visualization
Day 3	Model Training & Evaluation
Day 4	Feature Engineering & Hyperparameter Tuning

📁 Dataset Overview
**Source**: [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Format**: CSV (`creditcard.csv`)

Size: 284,807 transactions

Features: 30 (28 anonymized: V1–V28 + Time, Amount)

Target Variable: Class — 1 = Fraud, 0 = Normal

📊 Day 2: Exploratory Data Analysis (EDA)
✅ Actions:
Loaded data from Google Drive

Verified data integrity (null checks, types)

Investigated class imbalance

Created:

Class distribution bar chart

Histograms and KDE plots

Boxplots for skewed features

Correlation heatmaps

Log-scaled visualizations for fraud vs. amount

🔍 Insights:
Severe class imbalance: ~0.17% fraud

Strong fraud indicators: Features like V14, V12, and V17

Fraudulent transactions often have lower amounts

Time didn’t show strong correlation with fraud

🤖 Day 3: Initial Model Building & Evaluation
📌 Models Trained:
Logistic Regression

Decision Tree

K-Nearest Neighbors (KNN)

Naive Bayes

🧪 Evaluation Metrics:
Accuracy, Precision, Recall, F1 Score, ROC-AUC

Model	Accuracy	Precision	Recall	F1 Score	ROC AUC
Naive Bayes	0.976	0.059	0.847	0.087	0.963
Logistic Regression	0.999	0.829	0.643	0.723	0.957
KNN	0.999	0.919	0.806	0.858	0.944
Decision Tree	0.999	0.895	0.786	0.837	0.901

📌 Observations:
Logistic Regression had high precision, but moderate recall

Naive Bayes had very high recall, but too many false positives

KNN and Decision Tree offered balanced performance

🛠️ Day 4: Feature Engineering & Advanced Models
🔧 Enhancements:
Scaled Time and Amount using StandardScaler

Addressed imbalance using class_weight='balanced'

Applied GridSearchCV for parameter tuning

✅ Models Tuned:
Random Forest

Gradient Boosting

Decision Tree (as baseline)

Model	ROC AUC	F1 Score	Precision	Recall
Random Forest	0.983	0.933	0.992	0.880
Gradient Boosting	0.982	0.927	0.971	0.887
Decision Tree	0.933	0.912	0.970	0.860

🧠 Best Random Forest Parameters:
python
Copy code
{'n_estimators': 200, 'max_depth': 20, 'min_samples_split': 2}
⚖️ Class Distribution
Original:

Normal: 284,315

Fraud: 492

Balanced for Training:

Class 0 (Normal): 492

Class 1 (Fraud): 492

📌 Conclusion
This project demonstrates the end-to-end development of a fraud detection system — from raw data to a tuned ensemble model. With high AUC and F1 scores, especially from Random Forest and Gradient Boosting, the models show strong potential for real-world deployment in finance and security domains.
