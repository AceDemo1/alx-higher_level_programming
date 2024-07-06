-- import dump file
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show.id
GROUP BY tv_show.title
ORDER BY tv_show_ratings.rate DESC