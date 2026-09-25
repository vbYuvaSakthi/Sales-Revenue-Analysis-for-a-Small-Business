CREATE TABLE sales_transactions (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Date DATE,
    Customer_ID VARCHAR(50),
    Product_Category VARCHAR(50),
    Product_Name VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Total_Amount DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Month VARCHAR(20),
    Year INT,
    Quarter INT,
    Weekday VARCHAR(20)
);