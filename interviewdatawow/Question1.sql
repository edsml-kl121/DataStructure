-- write your code in PostgreSQL 9.4

SELECT name
FROM(
SELECT name, RANK() OVER(ORDER BY turn DESC) FROM line last_person
WHERE (SELECT sum(weight) from line where turn <= last_person.turn) <= 1000
LIMIT 1
) AS x;

