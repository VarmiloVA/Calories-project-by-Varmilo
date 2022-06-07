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

create table user (
    id int not null auto_increment,
    username varchar(255) not null,
    email varchar(255) not null,
    age int not null,
    primary key(id)
);
insert into user(username, email, age) values
	('VarmiloVA', 'varmilo.blue@protonmail.com', 15),
    ('Psylo', 'psylo@outlook.com', 31);

create table credential (
    id int not null auto_increment,
    password varchar(255) not null,
    user int,
    foreign key (user) references user(id)
);

show tables;
select * from calories;
select * from user;