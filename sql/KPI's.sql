# Total Revenue
SELECT SUM(Total_Amount) AS Total_Revenue
FROM sales_transactions;

# Total Transactions
SELECT COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM customer_info;

# Avg order value
SELECT ROUND(AVG(Total_Amount),2) AS Avg_Order_Value
FROM sales_transactions;

#Revenue by Product Category
SELECT
    Product_Category,
    SUM(Total_Amount) AS Revenue
FROM sales_transactions
GROUP BY Product_Category
ORDER BY Revenue DESC;

#Top 10 Products
SELECT
    Product_Name,
    SUM(Total_Amount) AS Revenue
FROM sales_transactions
GROUP BY Product_Name
ORDER BY Revenue DESC
LIMIT 10;

#Customer by gender
SELECT
    Gender,
    COUNT(*) AS Customer_Count
FROM customer_info
GROUP BY Gender;

















