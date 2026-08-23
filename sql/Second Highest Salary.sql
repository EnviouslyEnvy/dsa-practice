# Write your MySQL query statement below
# 176. Second Highest Salary
SELECT(SELECT DISTINCT Salary
FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 1 OFFSET 1)
as SecondHighestSalary

-- SELECT MAX(salary) AS SecondHighestSalary FROM Employee WHERE salary < (SELECT MAX(salary)FROM Employee)