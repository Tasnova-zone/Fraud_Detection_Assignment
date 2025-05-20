# Credit Card Fraud Detection - Data Exploration & Visualization

This repository contains a Jupyter Notebook focused on exploring and visualizing the **Credit Card Fraud Detection** dataset. The main objective is to uncover patterns and trends in fraudulent transactions, enabling better understanding and support for machine learning model development.

## 📂 Dataset

- **Source**: [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Format**: CSV (`creditcard.csv`)
- **Description**: Includes European credit card transactions, each labeled as fraudulent (1) or legitimate (0). Features `V1` to `V28` are principal components obtained via PCA, along with `Time`, `Amount`, and `Class`.

## 📊 Contents

### 1. Data Loading & Inspection
- Importing dataset using Pandas
- Checking data types, shape, null values, and basic statistics

### 2. Visualizations
- Class distribution plot (with log scale to handle imbalance)
- Histogram of transaction `Amount` for fraud vs. non-fraud
- Correlation heatmap (full features and top fraud-correlated ones)
- Boxplots and scatter plots for `Amount` and `Time` vs. `Class`
- Feature distribution comparisons for selected V-features (e.g., V10, V12, V14, V17)

### 3. Observations & Insights

1. Fraudulent transactions are very rare compared to legitimate ones, resulting in significant class imbalance in the dataset.  
2. Fraudulent transactions often involve smaller amounts, possibly to avoid triggering detection systems.  
3. Certain transaction features (e.g., V14, V12, V10, V17) have a strong correlation with fraudulent activity, indicating key behavioral differences.  
4. Transaction time by itself does not strongly indicate fraud, suggesting the need for additional feature engineering or temporal grouping.  
5. Due to the subtle and imbalanced nature of fraud cases, specialized detection techniques such as resampling or anomaly detection are necessary for effective identification.  

## 💻 Requirements

- Python 3.x
- Jupyter Notebook / Google Colab

### Required Libraries:
```bash
pip install pandas numpy matplotlib seaborn
