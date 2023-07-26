# Write your MySQL query statement below
select e2.name as Employee from Employee e1 inner join Employee e2 on e2.managerId=e1.id where e2.salary>e1.salary  ;