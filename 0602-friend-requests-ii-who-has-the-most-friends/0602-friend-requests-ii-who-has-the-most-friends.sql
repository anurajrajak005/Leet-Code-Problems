# Write your MySQL query statement below
select id , count(*) As num
From (
    select requester_id As id from RequestAccepted 
union All
    select Accepter_id from RequestAccepted
)
As friend_count
Group by id 
order by num Desc
limit 1
