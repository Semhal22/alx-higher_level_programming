--  lists all shows contained in the database hbtn_0d_tvshows
--  Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
  FROM tv_shows LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
  ORDER BY tv_shows.title, tv_show_genres.genre_id;