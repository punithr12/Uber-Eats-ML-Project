# Uber Eats ML Project — Data Dictionary

## Project Overview

This project uses synthetic Uber Eats marketplace data for:

- Customer segmentation
- Restaurant segmentation
- Sentiment analysis
- Delivery-time prediction
- Tip prediction
- Demand forecasting
- Business intelligence

---

# 1. Customers

**File:** `data/raw/customers.csv`

| Column | Description | Data Type |
|---|---|---|
| customer_id | Unique customer identifier | Integer |
| age | Customer age | Integer |
| gender | Customer gender | Categorical |
| city | Customer city | Categorical |
| signup_date | Date customer joined the platform | Date |
| preferred_cuisine | Preferred food category | Categorical |
| avg_order_value | Average customer order value | Float |
| total_orders | Total orders placed by customer | Integer |
| customer_rating | Average customer rating | Float |
| payment_preference | Preferred payment method | Categorical |

**Primary Key:** `customer_id`

---

# 2. Restaurants

**File:** `data/raw/restaurants.csv`

| Column | Description | Data Type |
|---|---|---|
| restaurant_id | Unique restaurant identifier | Integer |
| restaurant_name | Restaurant name | String |
| city | Restaurant city | Categorical |
| cuisine | Restaurant cuisine | Categorical |
| rating | Average restaurant rating | Float |
| avg_prep_time_min | Average food preparation time | Float |
| avg_order_value | Average order value | Float |
| total_orders | Total orders received | Integer |
| is_chain | Whether restaurant belongs to a chain | Boolean |
| restaurant_age_years | Number of years restaurant has operated | Float |

**Primary Key:** `restaurant_id`

---

# 3. Drivers

**File:** `data/raw/drivers.csv`

| Column | Description | Data Type |
|---|---|---|
| driver_id | Unique driver identifier | Integer |
| driver_age | Driver age | Integer |
| vehicle_type | Driver vehicle type | Categorical |
| experience_years | Driving experience | Float |
| rating | Average driver rating | Float |
| city | Driver operating city | Categorical |
| total_completed_deliveries | Number of completed deliveries | Integer |
| avg_delivery_time_min | Average delivery time | Float |
| acceptance_rate | Percentage of accepted delivery requests | Float |
| active_hours_per_week | Average weekly active hours | Float |

**Primary Key:** `driver_id`

---

# 4. Orders

**File:** `data/raw/orders.csv`

| Column | Description | Data Type |
|---|---|---|
| order_id | Unique order identifier | Integer |
| customer_id | Customer who placed the order | Integer |
| restaurant_id | Restaurant receiving the order | Integer |
| order_timestamp | Date and time order was placed | Datetime |
| order_amount | Base order amount | Float |
| discount_amount | Discount applied to order | Float |
| delivery_fee | Delivery fee charged | Float |
| tip_amount | Tip provided by customer | Float |
| payment_id | Associated payment identifier | Integer |
| order_status | Current order status | Categorical |
| items_count | Number of items ordered | Integer |
| is_weekend | Whether order occurred on weekend | Boolean |
| is_holiday | Whether order occurred on holiday | Boolean |

**Primary Key:** `order_id`

**Foreign Keys:**

- `customer_id → customers.customer_id`
- `restaurant_id → restaurants.restaurant_id`
- `payment_id → payments.payment_id`

---

# 5. Deliveries

**File:** `data/raw/deliveries.csv`

| Column | Description | Data Type |
|---|---|---|
| delivery_id | Unique delivery identifier | Integer |
| order_id | Associated order | Integer |
| driver_id | Driver assigned to delivery | Integer |
| delivery_distance_km | Delivery distance in kilometers | Float |
| weather_condition | Weather during delivery | Categorical |
| traffic_condition | Traffic level during delivery | Categorical |
| preparation_time_min | Restaurant preparation time | Float |
| pickup_time | Time food was picked up | Datetime |
| delivery_time | Time order was delivered | Datetime |
| delivery_duration_min | Total delivery duration | Float |
| delivery_status | Delivery outcome | Categorical |

**Primary Key:** `delivery_id`

**Foreign Keys:**

- `order_id → orders.order_id`
- `driver_id → drivers.driver_id`

---

# 6. Reviews

**File:** `data/raw/reviews.csv`

| Column | Description | Data Type |
|---|---|---|
| review_id | Unique review identifier | Integer |
| order_id | Associated order | Integer |
| customer_id | Customer who submitted review | Integer |
| restaurant_id | Restaurant being reviewed | Integer |
| rating | Customer rating from 1 to 5 | Integer |
| review_text | Customer written feedback | String |
| review_timestamp | Date and time review was submitted | Datetime |

**Primary Key:** `review_id`

**Foreign Keys:**

- `order_id → orders.order_id`
- `customer_id → customers.customer_id`
- `restaurant_id → restaurants.restaurant_id`

---

# 7. Payments

**File:** `data/raw/payments.csv`

| Column | Description | Data Type |
|---|---|---|
| payment_id | Unique payment identifier | Integer |
| order_id | Associated order | Integer |
| payment_method | Payment method used | Categorical |
| transaction_amount | Total transaction amount | Float |
| payment_status | Payment outcome | Categorical |
| transaction_timestamp | Payment processing timestamp | Datetime |
| refund_amount | Amount refunded to customer | Float |

**Primary Key:** `payment_id`

**Foreign Key:**

- `order_id → orders.order_id`

---

# Dataset Relationships

```text
Customers
    |
    | customer_id
    ↓
Orders ← Restaurants
    |
    | order_id
    ├──────────────→ Deliveries ← Drivers
    |
    ├──────────────→ Reviews
    |
    └──────────────→ Payments


    ML Use Cases
Customer Segmentation

Primary datasets:

Customers
Orders

Potential features:

Total orders
Average order value
Purchase frequency
Preferred cuisine
Customer rating
Restaurant Segmentation

Primary datasets:

Restaurants
Orders
Reviews

Potential features:

Restaurant rating
Order volume
Average order value
Preparation time
Sentiment score
Sentiment Analysis

Primary dataset:

Reviews

Target:

Customer sentiment

Input:

review_text
Delivery Time Prediction

Primary datasets:

Orders
Deliveries
Restaurants
Drivers

Potential features:

Delivery distance
Traffic condition
Weather condition
Preparation time
Driver experience
Vehicle type

Target:

delivery_duration_min
Tip Prediction

Primary datasets:

Orders
Deliveries
Customers

Potential features:

Order amount
Delivery distance
Delivery duration
Customer behavior
Weekend indicator

Target:

tip_amount
Demand Forecasting

Primary dataset:

Orders

Potential features:

Order timestamp
Hour
Day
Weekend
Holiday
City

Target:

Number of orders per hour