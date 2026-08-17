
import numpy as np
import pandas as pd

# --------------------------------------------------
# Configuration
# --------------------------------------------------

RANDOM_SEED = 42

NUM_CUSTOMERS = 5000
NUM_RESTAURANTS = 500

np.random.seed(RANDOM_SEED)


# --------------------------------------------------
# Generate Customers
# --------------------------------------------------

def generate_customers():

    customer_ids = np.arange(10001, 10001 + NUM_CUSTOMERS)

    ages = np.random.randint(18, 65, NUM_CUSTOMERS)

    genders = np.random.choice(
        ["Male", "Female", "Other"],
        size=NUM_CUSTOMERS,
        p=[0.48, 0.48, 0.04]
    )

    cities = np.random.choice(
        ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune"],
        size=NUM_CUSTOMERS
    )

    signup_dates = pd.to_datetime(
        np.random.choice(
            pd.date_range("2024-01-01", "2026-07-31"),
            size=NUM_CUSTOMERS
        )
    )

    customer_segments = np.random.choice(
        ["New", "Regular", "VIP"],
        size=NUM_CUSTOMERS,
        p=[0.30, 0.55, 0.15]
    )

    avg_monthly_orders = np.where(
        customer_segments == "New",
        np.random.uniform(1, 4, NUM_CUSTOMERS),
        np.where(
            customer_segments == "Regular",
            np.random.uniform(4, 10, NUM_CUSTOMERS),
            np.random.uniform(8, 20, NUM_CUSTOMERS)
        )
    )

    preferred_cuisines = np.random.choice(
        [
            "Indian",
            "Chinese",
            "Pizza",
            "Burgers",
            "South Indian",
            "Biryani",
            "Desserts"
        ],
        size=NUM_CUSTOMERS
    )

    avg_order_value = np.where(
        customer_segments == "New",
        np.random.uniform(150, 400, NUM_CUSTOMERS),
        np.where(
            customer_segments == "Regular",
            np.random.uniform(250, 700, NUM_CUSTOMERS),
            np.random.uniform(500, 1500, NUM_CUSTOMERS)
        )
    )

    payment_preferences = np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Wallet", "Cash"],
        size=NUM_CUSTOMERS,
        p=[0.45, 0.20, 0.15, 0.15, 0.05]
    )

    customers = pd.DataFrame({
        "customer_id": customer_ids,
        "age": ages,
        "gender": genders,
        "city": cities,
        "signup_date": signup_dates,
        "customer_segment": customer_segments,
        "avg_monthly_orders": np.round(avg_monthly_orders, 2),
        "preferred_cuisine": preferred_cuisines,
        "avg_order_value": np.round(avg_order_value, 2),
        "payment_preference": payment_preferences
    })

    return customers


# --------------------------------------------------
# Generate Restaurants
# --------------------------------------------------

def generate_restaurants():

    restaurant_ids = np.arange(20001, 20001 + NUM_RESTAURANTS)

    restaurant_names = [
        f"Restaurant_{i}"
        for i in range(1, NUM_RESTAURANTS + 1)
    ]

    cities = np.random.choice(
        ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune"],
        size=NUM_RESTAURANTS
    )

    cuisines = np.random.choice(
        [
            "Indian",
            "Chinese",
            "Pizza",
            "Burgers",
            "South Indian",
            "Biryani",
            "Desserts"
        ],
        size=NUM_RESTAURANTS
    )

    restaurant_categories = np.random.choice(
        ["Budget", "Mid-range", "Premium"],
        size=NUM_RESTAURANTS,
        p=[0.35, 0.50, 0.15]
    )

    ratings = np.clip(
        np.random.normal(4.0, 0.45, NUM_RESTAURANTS),
        1,
        5
    )

    avg_prep_time = np.where(
        cuisines == "Pizza",
        np.random.randint(15, 30, NUM_RESTAURANTS),
        np.where(
            cuisines == "Biryani",
            np.random.randint(20, 40, NUM_RESTAURANTS),
            np.random.randint(10, 30, NUM_RESTAURANTS)
        )
    )

    avg_order_value = np.where(
        restaurant_categories == "Budget",
        np.random.uniform(150, 350, NUM_RESTAURANTS),
        np.where(
            restaurant_categories == "Mid-range",
            np.random.uniform(300, 700, NUM_RESTAURANTS),
            np.random.uniform(600, 1500, NUM_RESTAURANTS)
        )
    )

    total_orders = np.random.randint(
        100,
        10000,
        NUM_RESTAURANTS
    )

    is_chain = np.random.choice(
        [True, False],
        size=NUM_RESTAURANTS,
        p=[0.35, 0.65]
    )

    restaurants = pd.DataFrame({
        "restaurant_id": restaurant_ids,
        "restaurant_name": restaurant_names,
        "city": cities,
        "cuisine_type": cuisines,
        "restaurant_category": restaurant_categories,
        "rating": np.round(ratings, 2),
        "avg_prep_time_min": avg_prep_time,
        "avg_order_value": np.round(avg_order_value, 2),
        "total_orders": total_orders,
        "is_chain": is_chain
    })

    return restaurants


# --------------------------------------------------
# Generate Drivers
# --------------------------------------------------

NUM_DRIVERS = 1000


# --------------------------------------------------
# Generate Drivers
# --------------------------------------------------

NUM_DRIVERS = 1000


def generate_drivers():

    driver_ids = np.arange(
        30001,
        30001 + NUM_DRIVERS
    )

    driver_age = np.random.randint(
        21,
        55,
        NUM_DRIVERS
    )

    vehicle_type = np.random.choice(
        ["Bike", "Scooter", "Car"],
        size=NUM_DRIVERS,
        p=[0.45, 0.40, 0.15]
    )

    experience_years = np.round(
        np.random.uniform(
            0.5,
            10,
            NUM_DRIVERS
        ),
        1
    )

    rating = np.clip(
        np.random.normal(
            4.2,
            0.35,
            NUM_DRIVERS
        ),
        1,
        5
    )

    cities = np.random.choice(
        [
            "Bangalore",
            "Mumbai",
            "Delhi",
            "Hyderabad",
            "Chennai",
            "Pune"
        ],
        size=NUM_DRIVERS
    )

    total_completed_deliveries = np.maximum(
        50,
        (
            experience_years
            * np.random.uniform(
                300,
                700,
                NUM_DRIVERS
            )
        ).astype(int)
    )

    avg_delivery_time = np.clip(
        np.random.normal(
            35,
            7,
            NUM_DRIVERS
        ),
        20,
        60
    )

    acceptance_rate = np.clip(
        np.random.normal(
            0.85,
            0.08,
            NUM_DRIVERS
        ),
        0.50,
        1.00
    )

    active_hours_per_week = np.round(
        np.random.uniform(
            15,
            60,
            NUM_DRIVERS
        ),
        1
    )

    drivers = pd.DataFrame({
        "driver_id": driver_ids,
        "driver_age": driver_age,
        "vehicle_type": vehicle_type,
        "experience_years": experience_years,
        "rating": np.round(rating, 2),
        "city": cities,
        "total_completed_deliveries": total_completed_deliveries,
        "avg_delivery_time_min": np.round(
            avg_delivery_time,
            2
        ),
        "acceptance_rate": np.round(
            acceptance_rate,
            2
        ),
        "active_hours_per_week": active_hours_per_week
    })

    return drivers


# --------------------------------------------------
# Generate Orders
# --------------------------------------------------

NUM_ORDERS = 50000


def generate_orders(customers, restaurants):

    # --------------------------------------------------
    # Order IDs
    # --------------------------------------------------

    order_ids = np.arange(
        50001,
        50001 + NUM_ORDERS
    )

    # --------------------------------------------------
    # Customer and Restaurant relationships
    # --------------------------------------------------

    customer_ids = np.random.choice(
        customers["customer_id"],
        size=NUM_ORDERS
    )

    restaurant_ids = np.random.choice(
        restaurants["restaurant_id"],
        size=NUM_ORDERS
    )

    # --------------------------------------------------
    # Generate Order Timestamps
    # --------------------------------------------------

    start_date = pd.Timestamp(
        "2025-08-01"
    )

    end_date = pd.Timestamp(
        "2026-07-31 23:59:59"
    )

    random_seconds = np.random.randint(
        start_date.value // 10**9,
        end_date.value // 10**9,
        NUM_ORDERS
    )

    # IMPORTANT:
    # Convert to Series so that .dt works
    order_timestamp = pd.Series(
        pd.to_datetime(
            random_seconds,
            unit="s"
        )
    )

    # --------------------------------------------------
    # Extract Hour
    # --------------------------------------------------

    order_hour = order_timestamp.dt.hour

    # --------------------------------------------------
    # Hourly Demand Weight
    # --------------------------------------------------

    hour_weights = np.select(
        [
            (order_hour >= 7) & (order_hour <= 10),
            (order_hour >= 11) & (order_hour <= 14),
            (order_hour >= 18) & (order_hour <= 22)
        ],
        [
            1.2,
            1.6,
            2.0
        ],
        default=0.6
    )

    # --------------------------------------------------
    # Number of Items
    # --------------------------------------------------

    items_count = np.random.choice(
        [1, 2, 3, 4, 5],
        size=NUM_ORDERS,
        p=[0.20, 0.35, 0.25, 0.15, 0.05]
    )

    # --------------------------------------------------
    # Base Item Price
    # --------------------------------------------------

    base_item_price = np.random.uniform(
        100,
        450,
        NUM_ORDERS
    )

    # --------------------------------------------------
    # Order Amount
    # --------------------------------------------------

    order_amount = (
        base_item_price
        * items_count
        * np.random.uniform(
            0.8,
            1.2,
            NUM_ORDERS
        )
    )

    # Add slight demand effect
    order_amount = (
        order_amount
        * np.random.uniform(
            0.95,
            1.05,
            NUM_ORDERS
        )
    )

    # --------------------------------------------------
    # Discount
    # --------------------------------------------------

    discount_percentage = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20],
        size=NUM_ORDERS,
        p=[0.40, 0.20, 0.20, 0.15, 0.05]
    )

    discount_amount = (
        order_amount
        * discount_percentage
    )

    # --------------------------------------------------
    # Delivery Fee
    # --------------------------------------------------

    delivery_fee = np.round(
        np.random.uniform(
            20,
            100,
            NUM_ORDERS
        ),
        2
    )

    # --------------------------------------------------
    # Tip
    # --------------------------------------------------

    tip_percentage = np.random.choice(
        [0, 0.05, 0.10, 0.15],
        size=NUM_ORDERS,
        p=[0.20, 0.35, 0.35, 0.10]
    )

    tip_amount = (
        order_amount * tip_percentage
        + np.random.normal(
            0,
            10,
            NUM_ORDERS
        )
    )

    tip_amount = np.maximum(
        0,
        tip_amount
    )

    # --------------------------------------------------
    # Order Status
    # --------------------------------------------------

    order_status = np.random.choice(
        [
            "Completed",
            "Cancelled",
            "Failed"
        ],
        size=NUM_ORDERS,
        p=[0.88, 0.09, 0.03]
    )

    # --------------------------------------------------
    # Weekend
    # --------------------------------------------------

   # --------------------------------------------------
# Weekend
# --------------------------------------------------

    is_weekend = (
    order_timestamp.dt.dayofweek >= 5
    )

    # --------------------------------------------------
    # Holiday
    # --------------------------------------------------

    # --------------------------------------------------
# Holiday
# --------------------------------------------------

    # --------------------------------------------------
# Holiday
# --------------------------------------------------

    holidays = pd.to_datetime([
    "2025-08-15",
    "2025-10-02",
    "2025-12-25",
    "2026-01-01",
    "2026-01-26",
    "2026-08-15"
])

    is_holiday = (
    order_timestamp.dt.normalize()
    .isin(holidays)
)

    # --------------------------------------------------
    # Payment IDs
    # --------------------------------------------------

    payment_ids = np.arange(
        70001,
        70001 + NUM_ORDERS
    )

    # --------------------------------------------------
    # Create Orders DataFrame
    # --------------------------------------------------

    orders = pd.DataFrame({
        "order_id": order_ids,
        "customer_id": customer_ids,
        "restaurant_id": restaurant_ids,
        "order_timestamp": order_timestamp,
        "order_amount": np.round(
            order_amount,
            2
        ),
        "discount_amount": np.round(
            discount_amount,
            2
        ),
        "delivery_fee": delivery_fee,
        "tip_amount": np.round(
            tip_amount,
            2
        ),
        "payment_id": payment_ids,
        "order_status": order_status,
        "items_count": items_count,
        "is_weekend": is_weekend,
        "is_holiday": is_holiday
    })

    return orders
# --------------------------------------------------
# Generate Deliveries
# --------------------------------------------------

def generate_deliveries(orders, restaurants, drivers):

    num_deliveries = len(orders)

    # Delivery IDs
    delivery_ids = np.arange(
        60001,
        60001 + num_deliveries
    )

    # Every order gets a driver
    driver_ids = np.random.choice(
        drivers["driver_id"],
        size=num_deliveries
    )

    # --------------------------------------------------
    # Delivery Distance
    # --------------------------------------------------

    delivery_distance_km = np.round(
        np.random.gamma(
            shape=2.5,
            scale=2.0,
            size=num_deliveries
        ),
        2
    )

    delivery_distance_km = np.clip(
        delivery_distance_km,
        1,
        20
    )

    # --------------------------------------------------
    # Weather
    # --------------------------------------------------

    weather_condition = np.random.choice(
        [
            "Clear",
            "Cloudy",
            "Rain",
            "Heavy Rain"
        ],
        size=num_deliveries,
        p=[0.50, 0.25, 0.20, 0.05]
    )

    # --------------------------------------------------
    # Traffic
    # --------------------------------------------------

    traffic_condition = np.random.choice(
        [
            "Low",
            "Medium",
            "High",
            "Severe"
        ],
        size=num_deliveries,
        p=[0.25, 0.45, 0.25, 0.05]
    )

    # --------------------------------------------------
    # Restaurant Preparation Time
    # --------------------------------------------------

    restaurant_prep_map = restaurants.set_index(
        "restaurant_id"
    )["avg_prep_time_min"]

    restaurant_ids = orders["restaurant_id"].values

    preparation_time_min = restaurant_prep_map.loc[
        restaurant_ids
    ].values

    # Add realistic variation
    preparation_time_min = (
        preparation_time_min
        + np.random.normal(
            0,
            3,
            num_deliveries
        )
    )

    preparation_time_min = np.clip(
        preparation_time_min,
        5,
        60
    )

    # --------------------------------------------------
    # Traffic Impact
    # --------------------------------------------------

    traffic_delay = np.select(
        [
            traffic_condition == "Low",
            traffic_condition == "Medium",
            traffic_condition == "High",
            traffic_condition == "Severe"
        ],
        [
            0,
            5,
            12,
            20
        ],
        default=5
    )

    # --------------------------------------------------
    # Weather Impact
    # --------------------------------------------------

    weather_delay = np.select(
        [
            weather_condition == "Clear",
            weather_condition == "Cloudy",
            weather_condition == "Rain",
            weather_condition == "Heavy Rain"
        ],
        [
            0,
            2,
            7,
            15
        ],
        default=0
    )

    # --------------------------------------------------
    # Base Travel Time
    # --------------------------------------------------

    base_travel_time = (
        delivery_distance_km / 0.45
    )

    # --------------------------------------------------
    # Delivery Duration
    # --------------------------------------------------

    delivery_duration_min = (
        preparation_time_min
        + base_travel_time
        + traffic_delay
        + weather_delay
        + np.random.normal(
            0,
            4,
            num_deliveries
        )
    )

    delivery_duration_min = np.clip(
        delivery_duration_min,
        10,
        120
    )

    delivery_duration_min = np.round(
        delivery_duration_min,
        2
    )

    # --------------------------------------------------
    # Delivery Status
    # --------------------------------------------------

    delivery_status = np.random.choice(
        [
            "Delivered",
            "Cancelled",
            "Failed"
        ],
        size=num_deliveries,
        p=[0.94, 0.04, 0.02]
    )

    # --------------------------------------------------
    # Pickup and Delivery Times
    # --------------------------------------------------

    order_timestamp = pd.to_datetime(
        orders["order_timestamp"]
    )

    pickup_time = (
        order_timestamp
        + pd.to_timedelta(
            preparation_time_min,
            unit="m"
        )
    )

    delivery_time = (
        pickup_time
        + pd.to_timedelta(
            delivery_duration_min,
            unit="m"
        )
    )

    # --------------------------------------------------
    # Create DataFrame
    # --------------------------------------------------

    deliveries = pd.DataFrame({
        "delivery_id": delivery_ids,
        "order_id": orders["order_id"].values,
        "driver_id": driver_ids,
        "delivery_distance_km": delivery_distance_km,
        "weather_condition": weather_condition,
        "traffic_condition": traffic_condition,
        "preparation_time_min": np.round(
            preparation_time_min,
            2
        ),
        "pickup_time": pickup_time,
        "delivery_time": delivery_time,
        "delivery_duration_min": delivery_duration_min,
        "delivery_status": delivery_status
    })

    return deliveries
# --------------------------------------------------
# Generate Reviews
# --------------------------------------------------

def generate_reviews(orders, customers, restaurants):

    # Only completed orders can have reviews
    completed_orders = orders[
        orders["order_status"] == "Completed"
    ].copy()

    num_reviews = len(completed_orders)

    # Review IDs
    review_ids = np.arange(
        80001,
        80001 + num_reviews
    )

    # Basic relationships
    order_ids = completed_orders["order_id"].values
    customer_ids = completed_orders["customer_id"].values
    restaurant_ids = completed_orders["restaurant_id"].values

    # --------------------------------------------------
    # Rating
    # --------------------------------------------------

    rating = np.random.choice(
        [1, 2, 3, 4, 5],
        size=num_reviews,
        p=[0.05, 0.08, 0.17, 0.35, 0.35]
    )

    # --------------------------------------------------
    # Review Text
    # --------------------------------------------------

    positive_reviews = [
        "Amazing food and fast delivery",
        "Great experience and delicious food",
        "Food was fresh and tasty",
        "Excellent service and quick delivery",
        "Really enjoyed the meal",
        "Very good food and packaging",
        "The food arrived hot and fresh",
        "Great restaurant, would order again",
        "Fast delivery and good quality food",
        "Very satisfied with my order"
    ]

    neutral_reviews = [
        "Food was okay",
        "Average experience",
        "The food was decent",
        "Delivery was okay",
        "Nothing special but acceptable",
        "Food quality was average",
        "Overall an average experience",
        "Order was fine",
        "The experience was satisfactory",
        "It was an okay meal"
    ]

    negative_reviews = [
        "Food arrived late and cold",
        "Very disappointing experience",
        "Food quality was poor",
        "Delivery was extremely slow",
        "The food was cold when it arrived",
        "Not happy with the service",
        "Order was delayed significantly",
        "Food was not fresh",
        "Poor packaging and bad experience",
        "Would not order again"
    ]

    review_text = []

    for r in rating:

        if r >= 4:
            review_text.append(
                np.random.choice(
                    positive_reviews
                )
            )

        elif r == 3:
            review_text.append(
                np.random.choice(
                    neutral_reviews
                )
            )

        else:
            review_text.append(
                np.random.choice(
                    negative_reviews
                )
            )

    # --------------------------------------------------
    # Review Timestamp
    # --------------------------------------------------

    order_timestamp = pd.to_datetime(
        completed_orders["order_timestamp"]
    )

    review_timestamp = (
        order_timestamp
        + pd.to_timedelta(
            np.random.randint(
                1,
                72,
                num_reviews
            ),
            unit="h"
        )
    )

    # --------------------------------------------------
    # Create DataFrame
    # --------------------------------------------------

    reviews = pd.DataFrame({
        "review_id": review_ids,
        "order_id": order_ids,
        "customer_id": customer_ids,
        "restaurant_id": restaurant_ids,
        "rating": rating,
        "review_text": review_text,
        "review_timestamp": review_timestamp
    })

    return reviews
# --------------------------------------------------
# Generate Payments
# --------------------------------------------------

def generate_payments(orders):

    num_payments = len(orders)

    payment_ids = orders["payment_id"].values

    order_ids = orders["order_id"].values

    # --------------------------------------------------
    # Payment Method
    # --------------------------------------------------

    payment_method = np.random.choice(
        [
            "UPI",
            "Credit Card",
            "Debit Card",
            "Wallet",
            "Cash"
        ],
        size=num_payments,
        p=[0.40, 0.25, 0.15, 0.15, 0.05]
    )

    # --------------------------------------------------
    # Transaction Amount
    # --------------------------------------------------

    transaction_amount = (
        orders["order_amount"].values
        - orders["discount_amount"].values
        + orders["delivery_fee"].values
        + orders["tip_amount"].values
    )

    transaction_amount = np.round(
        transaction_amount,
        2
    )

    # --------------------------------------------------
    # Payment Status
    # --------------------------------------------------

    payment_status = np.random.choice(
        [
            "Success",
            "Failed",
            "Refunded"
        ],
        size=num_payments,
        p=[0.94, 0.04, 0.02]
    )

    # --------------------------------------------------
    # Transaction Timestamp
    # --------------------------------------------------

    transaction_timestamp = pd.to_datetime(
        orders["order_timestamp"]
    ) + pd.to_timedelta(
        np.random.randint(
            1,
            10,
            num_payments
        ),
        unit="m"
    )

    # --------------------------------------------------
    # Refund Amount
    # --------------------------------------------------

    refund_amount = np.where(
        payment_status == "Refunded",
        transaction_amount,
        0
    )

    refund_amount = np.round(
        refund_amount,
        2
    )

    # --------------------------------------------------
    # Create DataFrame
    # --------------------------------------------------

    payments = pd.DataFrame({
        "payment_id": payment_ids,
        "order_id": order_ids,
        "payment_method": payment_method,
        "transaction_amount": transaction_amount,
        "payment_status": payment_status,
        "transaction_timestamp": transaction_timestamp,
        "refund_amount": refund_amount
    })

    return payments



# --------------------------------------------------
# Test Data Generation
# --------------------------------------------------

if __name__ == "__main__":

    customers = generate_customers()
    restaurants = generate_restaurants()
    drivers = generate_drivers()

    orders = generate_orders(
        customers,
        restaurants
    )
    deliveries = generate_deliveries(
    orders,
    restaurants,
    drivers
    )
    reviews = generate_reviews(
    orders,
    customers,
    restaurants
    )
    payments = generate_payments(
    orders
    )
    # Save datasets
    import os
    
    os.makedirs("data/raw", exist_ok=True)
    
    customers.to_csv("data/raw/customers.csv", index=False)
    restaurants.to_csv("data/raw/restaurants.csv", index=False)
    drivers.to_csv("data/raw/drivers.csv", index=False)
    orders.to_csv("data/raw/orders.csv", index=False)
    deliveries.to_csv("data/raw/deliveries.csv",index=False)
    reviews.to_csv("data/raw/reviews.csv",index=False)
    payments.to_csv("data/raw/payments.csv",index=False)
    
    print("\nDatasets saved successfully!")

    print("\nCustomers:")
    print(customers.head())
    print("\nCustomer Shape:")
    print(customers.shape)

    print("\nRestaurants:")
    print(restaurants.head())
    print("\nRestaurant Shape:")
    print(restaurants.shape)

    print("\nDrivers:")
    print(drivers.head())
    print("\nDriver Shape:")
    print(drivers.shape)

    print("\nOrders:")
    print(orders.head())
    print("\nOrder Shape:")
    print(orders.shape)

    print("\nDeliveries:")
    print(deliveries.head())

    print("\nDelivery Shape:")
    print(deliveries.shape)

    print("\nReviews:")
    print(reviews.head())

    print("\nReview Shape:")
    print(reviews.shape)
    print("\nPayments:")

    print(payments.head())

    print("\nPayment Shape:")
    print(payments.shape)

    