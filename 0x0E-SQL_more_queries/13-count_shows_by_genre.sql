-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run to import SQL dump:
-- 	* echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 	* curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
-- each record should display: tv_genres.name - number_shows
-- results must be sorted in descending order by number of shows linked
-- only one SELECT statement

SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_shows'
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
