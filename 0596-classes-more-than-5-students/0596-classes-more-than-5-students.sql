# Write your MySQL query statement below
SELECT c.class
FROM Courses as c
GROUP BY c.class
HAVING count(distinct c.student) >= 5