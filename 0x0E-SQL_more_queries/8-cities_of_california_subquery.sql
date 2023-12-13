-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name from cities where state_id = (
	SELECT id from states where name = 'California'
);