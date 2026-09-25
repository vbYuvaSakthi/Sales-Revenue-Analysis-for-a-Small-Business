import pandas as pd

customers_df = pd.read_csv("../data/customers_updated.csv")
transactions_df = pd.read_csv("../data/sales_updated.csv")

# Remove duplicate Customer IDs
customers_df.drop_duplicates(
    subset=["Customer_ID"],
    inplace=True
)

# Standardization
customers_df["Gender"] = (
    customers_df["Gender"]
    .str.strip()
    .str.title()
)

customers_df["Location"] = (
    customers_df["Location"]
    .str.strip()
    .str.title()
)

# Handle missing values

customers_df["Age"].fillna(
    customers_df["Age"].median(),
    inplace=True
)

customers_df["Total_Spent"].fillna(
    customers_df["Total_Spent"].median(),
    inplace=True
)

# Remove invalid values

customers_df = customers_df[
    customers_df["Age"].between(18, 100)
]

customers_df = customers_df[
    customers_df["Total_Spent"] >= 0
]

# Age Group Feature

customers_df["Age_Group"] = pd.cut(
    customers_df["Age"],
    bins=[18,25,35,50,100],
    labels=[
        "18-25",
        "26-35",
        "36-50",
        "50+"
    ]
)


transactions_df.drop_duplicates(
    subset=["Transaction_ID"],
    inplace=True
)

transactions_df["Date"] = pd.to_datetime(
    transactions_df["Date"],
    errors="coerce"
)

transactions_df["Product_Category"] = (
    transactions_df["Product_Category"]
    .str.strip()
    .str.title()
)

transactions_df["Payment_Method"] = (
    transactions_df["Payment_Method"]
    .str.strip()
    .str.title()
)

transactions_df = transactions_df[
    transactions_df["Quantity"] > 0
]

transactions_df = transactions_df[
    transactions_df["Unit_Price"] > 0
]

# Remove mismatched totals

transactions_df = transactions_df[
    transactions_df["Total_Amount"]
    ==
    transactions_df["Quantity"] *
    transactions_df["Unit_Price"]
]

# Feature Engineering

transactions_df["Month"] = (
    transactions_df["Date"]
    .dt.month_name()
)

transactions_df["Year"] = (
    transactions_df["Date"]
    .dt.year
)

transactions_df["Quarter"] = (
    transactions_df["Date"]
    .dt.quarter
)

# Save files

customers_df.to_csv(
    "../data/clean_customers.csv",
    index=False
)

transactions_df.to_csv(
    "../data/clean_transactions.csv",
    index=False
)

print("Transformation Completed")