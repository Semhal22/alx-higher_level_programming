-- Lists all cities contained in hbtn_0d)usa
-- Each record should display: cities.id - cities.name - states.name
SELECT cities.id AS id, cities.name AS name, states.name AS name
  FROM cities
  LEFT JOIN states
  ON cities.state_id = states.id
  ORDER BY cities.id;