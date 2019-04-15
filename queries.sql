USE honeybees;

select * from bees_data;
select * from pesticides;

-- Top 5 states with the highest honey/colony yield --
SELECT b.state, b.end_colonies, b.colony_yield, b.production
FROM bees_data as b
ORDER BY b.colony_yield DESC
LIMIT 5;

-- Production rates for the 5 states that ended the 2015 year with the most colonies --
SELECT b.state, b.end_colonies, b.colony_yield, b.production
FROM bees_data as b
ORDER BY b.end_colonies DESC
LIMIT 5;

-- Pesticide rates for the 5 states that saw the highest colony loss --
select b.state, b.colony_change, ROUND(sum(p.high_estimate))
from pesticides as p
right join bees_data as b
on p.state = b.state
GROUP BY p.state
ORDER BY b.colony_change ASC
LIMIT 5;

-- Pesticide rates for the 5 states that saw the most colonies added --
select b.state, b.colony_change, ROUND(sum(p.high_estimate))
from pesticides as p
right join bees_data as b
on p.state = b.state
GROUP BY p.state
ORDER BY b.colony_change DESC
LIMIT 5;

-- Colony change for the states with the greatest pesticide use --
select b.state, b.colony_change, ROUND(sum(p.high_estimate))
from pesticides as p
right join bees_data as b
on p.state = b.state
GROUP BY p.state
ORDER BY p.high_estimate DESC
LIMIT 5;
