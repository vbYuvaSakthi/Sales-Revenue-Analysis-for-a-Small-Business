SELECT
    Customer_Segment,
    COUNT(*) AS Customers
FROM customer_segment
GROUP BY Customer_Segment;