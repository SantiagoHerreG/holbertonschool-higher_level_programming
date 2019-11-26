-- Lists the number of records with the same score
-- Displays the number of records for this score with the label number
SELECT score, COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY score DESC;

