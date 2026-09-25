import pandas as pd

customers_df = pd.read_csv("../data/customers_updated.csv")
transactions_df = pd.read_csv("../data/sales_updated.csv")

print(" CUSTOMER DATA VALIDATION ")

# Null values
print("\nMissing Values:")
print(customers_df.isnull().sum())

# Duplicate Customer IDs
duplicate_customers = customers_df["Customer_ID"].duplicated().sum()
print("\nDuplicate Customer IDs:", duplicate_customers)

# Invalid Age
invalid_age = customers_df[
    (customers_df["Age"] < 18) |
    (customers_df["Age"] > 100)
]

print("Invalid Age Records:", len(invalid_age))

# Negative Spending
negative_spend = customers_df[
    customers_df["Total_Spent"] < 0
]

print("Negative Total_Spent Records:", len(negative_spend))


print("\n SALES TRANSACTION DATA VALIDATION ")

# Null values
print("\nMissing Values:")
print(transactions_df.isnull().sum())

# Duplicate Transactions
duplicate_transactions = (
    transactions_df["Transaction_ID"]
    .duplicated()
    .sum()
)

print("\nDuplicate Transaction IDs:", duplicate_transactions)

# Quantity check
invalid_quantity = transactions_df[
    transactions_df["Quantity"] <= 0
]

print("Invalid Quantity Records:", len(invalid_quantity))

# Unit Price check
invalid_price = transactions_df[
    transactions_df["Unit_Price"] <= 0
]

print("Invalid Unit Price Records:", len(invalid_price))

# Total Amount validation

amount_mismatch = transactions_df[
    transactions_df["Total_Amount"] !=
    (
        transactions_df["Quantity"] *
        transactions_df["Unit_Price"]
    )
]

print("Total Amount Mismatch Records:",
      len(amount_mismatch))

print("\nValidation Completed")