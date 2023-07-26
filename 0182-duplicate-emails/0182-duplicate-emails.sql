# Write your MySQL query statement below
SELECT distinct a.Email
FROM Person a,Person b
WHERE a.Id<>b.Id
AND a.Email=b.Email