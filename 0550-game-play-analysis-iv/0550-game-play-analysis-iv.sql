# Write your MySQL query statement below
select Round(count(DISTINCT player_id)/ (select count(DISTINCT player_id)
From Activity),2) AS fraction
from Activity
WHERE (player_id , DATE_SUB(event_date, INTERVAL 1 DAY)) IN(
    select player_id , min(event_date) AS first_login 
    from Activity 
    group by player_id
)