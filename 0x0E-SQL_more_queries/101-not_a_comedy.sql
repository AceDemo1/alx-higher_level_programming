-- import dump file
SELECT tv_show.title
FROM tv_show
WHERE tv_show.id NOT IN (
	SELECT tv_show_genres.show_id
	FROM tv_show_genres
	WHERE tv_show_genres.genres_id = (
		SELECT tv_genres.id
		FROM tv_genres
		WHERE name = Comedy))
