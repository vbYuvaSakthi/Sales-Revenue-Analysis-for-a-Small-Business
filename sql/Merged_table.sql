CREATE TABLE sales_customer_analysis AS
SELECT
    t.Transaction_ID,
    t.Date,
    t.Customer_ID,
    c.Name,
    c.Age,
    c.Gender,
    c.Location,
    c.Age_Group,
    c.Total_Spent,
    t.Product_Category,
    t.Product_Name,
    t.Quantity,
    t.Unit_Price,
    t.Total_Amount,
    t.Payment_Method,
    t.Month,
    t.Year,
    t.Quarter,
    t.Weekday
FROM sales_transactions t
JOIN customer_info c
ON t.Customer_ID = c.Customer_ID;