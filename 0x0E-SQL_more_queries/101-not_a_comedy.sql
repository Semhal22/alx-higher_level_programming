-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = (
	SELECT id FROM tv_genres
	WHERE name = 'Comedy'
)
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title;