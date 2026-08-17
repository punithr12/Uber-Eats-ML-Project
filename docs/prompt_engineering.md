# Prompt Engineering — Uber Eats Synthetic Data Generation

## Objective

Prompt engineering was used to design the Python script responsible for generating realistic synthetic Uber Eats marketplace data.

The generated data was designed to support:

- Customer segmentation
- Restaurant segmentation
- Sentiment analysis
- Delivery-time prediction
- Tip prediction
- Demand forecasting

---

# 1. Role-Based Prompting

The AI model was assigned the role of:

> Machine Learning Engineer and Data Scientist specializing in food-delivery and marketplace analytics.

This helps the model generate data using realistic ML and business requirements rather than producing completely random values.

---

# 2. P.T.C.F. Framework

The P.T.C.F. framework was used to structure the prompt.

## P — Persona

The model was instructed to act as an experienced Machine Learning Engineer working on a food-delivery analytics platform.

## T — Task

The model was asked to design Python code for generating synthetic datasets for:

- Customers
- Restaurants
- Drivers
- Orders
- Deliveries
- Reviews
- Payments

## C — Context

The synthetic data needed to represent a realistic Uber Eats-style marketplace.

The data needed relationships between entities so that it could later be used for machine learning.

Examples:

- Customers place orders.
- Restaurants receive orders.
- Drivers complete deliveries.
- Orders generate payments.
- Customers submit reviews.
- Deliveries contain distance, traffic and weather information.

## F — Format

The output was requested as:

- Python code
- Pandas DataFrames
- CSV-compatible datasets
- Clearly defined columns
- Realistic categorical and numerical values

---

# 3. Few-Shot Prompting

Examples were provided to guide the expected output.

For example:

### Example Customer

```text
customer_id: 10001
age: 28
gender: Female
city: Bangalore
preferred_cuisine: Biryani
avg_order_value: 350

prompt used for synthetic data generation

You are an experienced Machine Learning Engineer and Data Scientist
specializing in food delivery and marketplace analytics.

Your task is to design a realistic synthetic Uber Eats marketplace
dataset for an end-to-end machine learning project.

Generate Python code using Pandas and NumPy.

Create datasets for:

1. Customers
2. Restaurants
3. Drivers
4. Orders
5. Deliveries
6. Reviews
7. Payments

The datasets must have realistic relationships through primary keys
and foreign keys.

The data should support:

- Customer segmentation
- Restaurant segmentation
- Sentiment analysis
- Delivery time prediction
- Tip prediction
- Hourly demand forecasting

Use realistic distributions rather than completely random values.

For delivery time, create relationships between distance, traffic,
weather, restaurant preparation time and driver characteristics.

For reviews, make review text reasonably consistent with customer
ratings.

For payments, derive transaction amounts from order amounts,
discounts, delivery fees and tips.

Return modular Python functions and ensure that the resulting
datasets can be exported to CSV files.
