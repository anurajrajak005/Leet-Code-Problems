# Write your MySQL query statement below
select d.name as Department, 
       e1.name as Employee, 
       e1.salary as Salary
from Employee e1 inner join Department d
on e1.departmentID = d.id
where 3 > (
    select count(DISTINCT (e2.salary))
    from Employee e2
    where e2.salary > e1.salary AND
    e1.DepartmentId = e2.DepartmentId
)