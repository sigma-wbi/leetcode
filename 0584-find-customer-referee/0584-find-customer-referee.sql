# Write your MySQL query statement below
SELECT C.name
FROM Customer as C
WHERE referee_id != 2 OR referee_id is NULL