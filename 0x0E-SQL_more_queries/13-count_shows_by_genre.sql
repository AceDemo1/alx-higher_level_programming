-- import dump file 
SELECT genres, COUNT(*) AS number_of_shows
FROM tv_genres
WHERE genres NOT NULL
ORDER BY number_of_shows DESC;
