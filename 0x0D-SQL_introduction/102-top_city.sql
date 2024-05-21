-- Calculate the average temperature by city for July and August, and display the top 3 cities ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
