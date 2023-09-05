# Write your MySQL query statement below
select e.name as Customers from Customers e left join Orders o on e.id=o.customerId where o.customerId is null