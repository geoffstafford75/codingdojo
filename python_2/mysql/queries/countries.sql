select countries.name, languages.language,  languages.percentage
from countries
JOIN languages on languages.country_id = countries.id
where languages.language = "Slovene"
order by languages.percentage desc;

select countries.name, count(cities.id) as cities
from countries
join cities on cities.country_id = countries.id
group by countries.id
order by cities desc;

select cities.name, cities.population, cities.country_id from cities
where cities.country_code = "MEX"
and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage
from countries
join languages on languages.country_id = countries.id
where languages.percentage > 89
order by languages.percentage desc;

select countries.name,countries.surface_area, countries.population from countries
where countries.surface_area < 501 and
countries.population > 100000;

select countries.name, countries.government_form, countries.life_expectancy from countries
where countries.government_form = "Constitutional Monarchy"
and countries.life_expectancy > 75
and countries.capital > 200;

select countries.name as country_name, cities.name as city_name, cities.district, cities.population from countries
join cities on countries.id = cities.country_id
where countries.id = 9
and cities.district = "Buenos Aires"
and cities.population > 500000;

select countries.region, count(countries.id) as countries from countries
group by countries.region
order by count(countries.id) desc

