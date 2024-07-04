-- lists
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = California)
WHERE name = California;
ORDER BY id;
