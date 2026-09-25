import pandas as pd

customers_df = pd.read_csv("../data/customers_updated.csv")
transactions_df = pd.read_csv("../data/sales_updated.csv")

# Customer Tests

assert customers_df["Customer_ID"].is_unique, \
    "Duplicate Customer IDs Found"

assert customers_df["Age"].between(
    18,
    100
).all(), \
    "Invalid Age Values Found"

assert (
    customers_df["Total_Spent"] >= 0
).all(), \
    "Negative Total Spent Found"

# Transaction Tests

assert transactions_df["Transaction_ID"].is_unique, \
    "Duplicate Transaction IDs Found"

assert (
    transactions_df["Quantity"] > 0
).all(), \
    "Invalid Quantity Found"

assert (
    transactions_df["Unit_Price"] > 0
).all(), \
    "Invalid Unit Price Found"

assert (
    transactions_df["Total_Amount"]
    ==
    transactions_df["Quantity"]
    *
    transactions_df["Unit_Price"]
).all(), \
    "Total Amount Mismatch Found"

print("All Unit Tests Passed Successfully")