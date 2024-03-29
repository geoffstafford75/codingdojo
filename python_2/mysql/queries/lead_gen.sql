select monthname(str_to_date(month(billing.charged_datetime), '%m')) as month,sum(billing.amount) as revenue
from billing
where 
billing.charged_datetime >= '2012/03/01'
and billing.charged_datetime <= '2012/03/31'
group by month(billing.charged_datetime);

select billing.client_id, sum(billing.amount) as total_revenue
from billing
where billing.client_id = 2
group by client_id;

select domain_name as website, client_id from sites
where client_id = 10;

select sites.client_id, count(sites.site_id) as number_of_websites, monthname(str_to_date(month(sites.created_datetime), '%m')) as month_created, year(sites.created_datetime) as year from sites
where client_id = 1
group by month_created, year;

select sites.client_id, count(sites.site_id) as number_of_websites, monthname(str_to_date(month(sites.created_datetime), '%m')) as month_created, year(sites.created_datetime) as year from sites
where client_id = 20
group by month_created, year;

where client_id = 1

