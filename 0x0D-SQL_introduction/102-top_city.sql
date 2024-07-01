-- displays top 3 cities
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperature
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
