-- import dump file
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT tv_show_genres.show_id
	FROM tv_show_genres
	JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id
	WHERE tv_genres.name = Comedy)
ORDER BY tv_shows.title
