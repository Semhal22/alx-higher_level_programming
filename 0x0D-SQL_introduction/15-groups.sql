-- Lists the number of records with the same score in the table second_tab
-- Result displays score and number of records for this score
-- List is sorted by the number of records(descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC
