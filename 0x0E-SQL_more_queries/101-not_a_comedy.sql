-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run to import SQL dump:
-- 	* echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 	* curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all shows not linked to the "Comedy" genre in hbtn_0d_tvshows db
-- the tv_genres table contains only one record where name = Comedy (but the id can be different)
-- each record should display: tv_shows.title
-- results must be sorted in ascending order by show title
-- max of two SELECT statements

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
	SELECT tv_shows.title
	FROM tv_shows
	INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title ASC;
