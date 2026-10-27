SELECT 
    "Low Salary" AS category, 
    count(income) as accounts_count 
from Accounts 
where income < 20000 
UNION 
SELECT 
    "Average Salary" AS category, 
    count(income) as accounts_count 
from Accounts 
where income >= 20000 and income <= 50000 
UNION 
SELECT 
    "High Salary" AS category, 
    count(income) as accounts_count 
from Accounts 
where income > 50000;