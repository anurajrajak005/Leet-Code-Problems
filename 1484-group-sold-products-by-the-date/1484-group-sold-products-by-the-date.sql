# Write your MySQL query statement below
select sell_date,
        count(DISTINCT product) AS num_sold,
        GROUP_CONCAT(
            DISTINCT product
            order by product
            SEPARATOR  ','
        ) as Products
from 
Activities
group by sell_date
order by sell_date , products; 