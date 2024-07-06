-- import dump file
SELECT tv_show.title
FROM tv_show
WHERE tv_show.id NOT IN (
	SELECT tv_show_genres.show_id
	FROM tv_show_genres
	JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id
	WHERE name = Comedy)
ORDER BY tv_show.title
