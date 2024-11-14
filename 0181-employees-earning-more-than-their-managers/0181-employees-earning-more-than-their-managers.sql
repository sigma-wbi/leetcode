# Write your MySQL query statement below
SELECT e1.name as "Employee" # 결과 테이블 컬럼 이름
FROM Employee as e1, Employee as e2 # 결과 데이터를 e1으로, 비교할 매니저를 e2로
WHERE e1.managerId = e2.id
    AND e1.salary > e2.salary