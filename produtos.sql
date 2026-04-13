create database cadastro_produtos;

use cadastro_produtos;

create table produtos(
idProduto int not null auto_increment primary key,
produto varchar(100) not null,
preco float not null,
estoque int not null
);