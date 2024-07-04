-- lists cities
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE state.id = cities.state_id
ORDER BY cities.id
