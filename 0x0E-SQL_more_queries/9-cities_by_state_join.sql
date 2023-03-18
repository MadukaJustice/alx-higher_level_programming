-- lists all the cities in the database "hbtn_0d_usa"
-- each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- only one SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
