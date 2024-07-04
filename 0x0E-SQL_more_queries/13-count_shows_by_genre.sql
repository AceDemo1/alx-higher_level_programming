-- import dump file 
SELECT tv_genres.name AS genres, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genres_id = tv_genres.id
ORDER BY number_of_shows DESC;
