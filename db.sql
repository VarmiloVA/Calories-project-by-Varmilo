show databases;
create database nutritional_values;
use nutritional_values;

create table calories (
    id int not null auto_increment,
    name varchar(255) not null,
    calories int not null,
    primary key (id)
);

create table user (
    id int not null auto_increment,
    username varchar(255) not null,
    email varchar(255) not null,
    age int not null,
    primary key(id)
);

create table credential (
    id int not null auto_increment,
    password varchar(255) not null,
    user int,
    foreign key (user) references user(id)
);