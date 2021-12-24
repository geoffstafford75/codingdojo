select customer.first_name as first_name, 
customer.last_name as last_name, 
customer.email as email, 
address.address as address,
city.city,
country.country
from customer
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
join country on country.country_id = city.country_id
where city.city_id = 312;

select film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name from film
join film_category on film.film_id = film_category.film_id
join category on category.category_id = film_category.category_id
where category.category_id = (select category_id from category where name = "Comedy");

select actor.actor_id, concat(actor.first_name, ' ', actor.last_name), film.title, film.description, film.release_year from film
left join film_actor on film.film_id = film_actor.film_id
join actor on actor.actor_id = film_actor.actor_id
where actor.actor_id = 5;

select customer.first_name, customer.last_name, address.address from customer
join address on address.address_id = customer.address_id
join city on city.city_id = address.city_id
where customer.store_id = 1 and
city.city_id in (1,42,312,459);

select film.title, film.description, film.release_year, film.rating, film.special_features from film
join film_actor on film_actor.film_id = film.film_id
where actor_id = 15 and
film.rating = "G" and
film.special_features like "%behind the scenes%";

select film.film_id, film.title, actor.actor_id, concat(actor.first_name," ",actor.last_name) as actor_name from film
left join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where film.film_id = 369;


select film.title, 
film.description, 
film.release_year, 
film.rating, 
film.special_features, 
category.name from film
join film_category on film_category.film_id = film.film_id
join category on film_category.category_id = category.category_id
where film.rental_rate = 2.99
and category.category_id = (select category_id from category where name = "Drama");

select film.title, 
film.description,
film.release_year, 
film.rating, 
film.special_features,
actor.first_name,
actor.last_name,
category.name from film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
join film_actor on film_actor.film_id=film.film_id
join actor on actor.actor_id = film_actor.actor_id
where actor.first_name = "SANDRA" and
actor.last_name = "KILMER" and
category.name = "action"