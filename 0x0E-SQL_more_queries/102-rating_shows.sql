-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run to import SQL dump:
-- 	* echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 	* curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- lists all shows in hbtn_0d_tvshows db by their rating
-- each record should display: tv_shows.title - rating sum
-- results must be sorted in descendong order by rating
-- max of two SELECT statements

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
