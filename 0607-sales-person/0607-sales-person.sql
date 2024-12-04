# Write your MySQL query statement below
SELECT S.NAME
FROM SALESPERSON S
WHERE S.SALES_ID NOT IN (
                            SELECT O.SALES_ID 
                            FROM ORDERS O INNER JOIN COMPANY C 
                                ON O.COM_ID = C.COM_ID
                                AND C.NAME = 'RED'
                        );