#Customer segmentation
CREATE TABLE customer_segment AS
SELECT
    Customer_ID,
    Name,
    Total_Spent,
    CASE
        WHEN Total_Spent >= 5000 THEN 'High Value'
        WHEN Total_Spent >= 2000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Customer_Segment
FROM customer_info;





