-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run to import SQL dump:
-- 	* echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 	* curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all shows and all genres linked to that show in hbtn_0d_tvshows db
-- if a show doesn't have a genre, display NULL in the genre column
-- each record should display: tv_shows.title - tv_genres.name
-- results must be sorted in ascending order by show title and genre name
-- only one SELECT statement

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
