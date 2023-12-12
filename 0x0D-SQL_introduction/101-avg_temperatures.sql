-- Computes the temp average of all records in the table temperatures
-- Result is city and the avg_temp
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
