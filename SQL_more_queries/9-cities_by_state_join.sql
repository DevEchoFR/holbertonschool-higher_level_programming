-- Lists all cities with their state name using JOIN, sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
