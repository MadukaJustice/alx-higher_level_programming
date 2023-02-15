-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run to import SQL dump:
-- 	* echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 	* curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all genres not linked to "Dexter" in hbtn_0d_tvshows db
-- the tv_shows table contains only one record where title = Dexter (but the id can be different)
-- each record should display:tv_genres.name
-- results must be sorted in ascending order by genre name
-- max of two SELECT statements

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name ASC;
