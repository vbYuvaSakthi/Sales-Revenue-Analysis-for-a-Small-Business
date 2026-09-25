import pandas as pd

customers_df = pd.read_csv("../data/customers_updated.csv")
transactions_df = pd.read_csv("../data/sales_updated.csv")

print("\nCustomer Data Shape:", customers_df.shape)
print("Transaction Data Shape:", transactions_df.shape)

print("\nCustomer Columns")
print(customers_df.columns)

print("\nSales Transaction Columns")
print(transactions_df.columns)