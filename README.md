# Uber Eats ML Project

## Project Overview

This project develops an end-to-end Machine Learning solution for Uber Eats using synthetic customer, restaurant, order, delivery, payment, and customer feedback data.

The project focuses on understanding customer and restaurant behavior, analyzing customer feedback, predicting delivery performance, forecasting order demand, and converting ML results into actionable business insights.

---

## Final Presentation

👉 [View Uber Eats ML Project Presentation](https://docs.google.com/presentation/d/11SMZWBqTgvhEOqtSMI1l_0X2mOgdAIwMveIBbmhYDXI/edit?usp=sharing)

---

## Business Objective

The objective is to build an integrated ML system that can help Uber Eats:

- Identify valuable customer segments.
- Identify restaurant segments and operational issues.
- Understand customer sentiment and negative experiences.
- Predict delivery duration.
- Understand factors affecting delivery performance.
- Forecast future order demand.
- Support operational planning and rider capacity decisions.

---

## Machine Learning Workflow

```text
Raw Uber Eats Data
        ↓
Data Preparation & Cleaning
        ↓
Feature Engineering
        ↓
Customer & Restaurant Segmentation
        ↓
NLP & Sentiment Analysis
        ↓
Delivery Time & Tip Prediction
        ↓
Hourly Demand Forecasting
        ↓
Model Evaluation
        ↓
End-to-End ML Integration
        ↓
Business Insights & Recommendations

Uber-Eats-ML-Project/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── deliveries.csv
│   │   ├── drivers.csv
│   │   ├── orders.csv
│   │   ├── payments.csv
│   │   ├── restaurants.csv
│   │   └── reviews.csv
│   │
│   └── processed/
│       ├── customer_features.csv
│       ├── customer_segmentation.csv
│       ├── demand_forecast_7_days.csv
│       ├── hourly_demand.csv
│       └── restaurant_segmentation.csv
│
├── notebooks/
│   ├── Day_2_Customer_Restaurant_Segmentation.ipynb
│   ├── Day_3_Customer_Feedback_NLP.ipynb
│   ├── Day_4_Delivery_Time_Tip_Prediction.ipynb
│   ├── Day_5_Hourly_Demand_Forecasting.ipynb
│   └── Day_6_End_to_End_ML_Pipeline_Business_Insights.ipynb
│
├── src/
│   ├── generate_data.py
│   └── __init__.py
│
├── docs/
│   ├── data_dictionary.md
│   └── prompt_engineering.md
│
├── requirements.txt
├── README.md
└── .gitignore


```markdown
ML Components
Day 2 — Customer & Restaurant Segmentation
Customer feature engineering
Restaurant feature engineering
StandardScaler
K-Means clustering
DBSCAN clustering
PCA analysis
Cluster interpretation
Business-oriented customer and restaurant segments
Day 3 — Customer Feedback NLP
Text preprocessing
Sentiment analysis
TF-IDF feature extraction
Sentiment classification
Model evaluation
Customer feedback insights
Day 4 — Delivery Time & Tip Prediction
Feature engineering
Regression modelling
Linear Regression
Ridge Regression
Lasso Regression
Random Forest
MAE evaluation
RMSE evaluation
R² evaluation
Model comparison
Day 5 — Hourly Demand Forecasting
Hourly demand aggregation
Time-series analysis
Stationarity analysis
Time-series decomposition
ARIMA
Prophet
Forecast evaluation
7-day demand forecasting
Prediction intervals
Day 6 — End-to-End ML Pipeline & Business Insights
Integration of outputs from previous ML stages
Customer segmentation insights
Restaurant segmentation insights
NLP sentiment insights
Delivery prediction insights
Demand forecasting insights
Business recommendations
Operational decision support
Business Impact

The ML solution can support Uber Eats in:

Customer retention and personalization
Identifying high-value customers
Restaurant performance optimization
Improving customer experience
Monitoring negative customer feedback
Delivery-time optimization
Rider capacity planning
Demand-based operational planning
Data-driven business decision making
Documentation

The project includes:

Data dictionary
Prompt engineering documentation
ML notebooks
Synthetic datasets
Processed datasets
End-to-end ML workflow
Business insights
Final presentation
Technologies Used
Python
Pandas
NumPy
Scikit-learn
SciPy
Matplotlib
Seaborn
NLTK
Statsmodels
Prophet
Jupyter Notebook
Git
