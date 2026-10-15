# Write your MySQL query statement below
select
    Round(sum(if(order_date = customer_pref_delivery_date, 1,0))*100/count(Distinct customer_id), 2)
    AS immediate_percentage  
    from Delivery
where (customer_id, order_date) 
IN(select customer_id , min(order_date) as first_date
from delivery 
group by customer_id 
);

