-- displays the max temperature of each state (ordered by State name) 
-- Result is state and max_temp
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
