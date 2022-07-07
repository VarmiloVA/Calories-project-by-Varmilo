show databases;
create database nutritional_values;
use nutritional_values;

create table calories (
    id int not null auto_increment,
    name varchar(255) not null,
    calories int not null,
    primary key (id)
);
insert into calories(name, calories) values
	('Pizza', 500),
    ('Ice Cream', 300),
    ('CocaCola', 80);
caloriesname
show tables;
select * from calories;