-- dispalys avg temp.
USE hbtn_0c_0
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
