-- SELECT rows with the same score and getting their count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
