create database ecotracking;
use ecotracking;
create table velocidade (idVelocidade integer not null primary key, volta integer not null);
insert into velocidade values(01, 10);
insert into velocidade values(02, 15);
select * from velocidade;
