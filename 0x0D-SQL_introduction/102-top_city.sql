-- Calculate the average temperature by city for July and August, and display the top 3 cities ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM table_name
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
