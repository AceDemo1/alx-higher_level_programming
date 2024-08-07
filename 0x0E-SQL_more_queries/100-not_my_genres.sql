-- import dump file
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.id NOT IN (
	SELECT genre_id
	FROM tv_show_genres
 	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    	WHERE tv_shows.title = 'Dexter'
)
GROUP BY tv_genres.name
ORDER BY tv_genres.name;
