select city , count(order_details) as total_orders ,count(distinct cust_id) as number_of_customers ,sum(total_order_cost) as total_order_cost from
customers inner join orders 
on customers.id = orders.cust_id 
group by city ;