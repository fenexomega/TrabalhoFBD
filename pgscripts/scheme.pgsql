CREATE USER user_restaurante WITH PASSWORD 'delivery';
CREATE USER admin_restaurante WITH PASSWORD 'root';

CREATE DATABASE deliverydb OWNER admin_restaurante;

# conectar ao banco
\c deliverydb

CREATE TABLE funcionario (
  cpf char(13) PRIMARY KEY,
  nome varchar(200) NOT NULL,
  salario decimal(10,2) NOT NULL
  );

CREATE TABLE cliente (
  telefone varchar(20) PRIMARY KEY,
  aniversario date NOT NULL,
  rua varchar (200) NOT NULL,
  bairro varchar(100) NOT NULL,
  complemento varchar(500)
  );

CREATE TABLE atendente (
  fcpf char(13) REFERENCES funcionario(cpf) UNIQUE,
  login varchar(20) PRIMARY KEY,
  senha char(16)
  );

CREATE TABLE prato(
  valor DECIMAL(5,2) NOT NULL,
  nome varchar(200) NOT NULL,
  codigo serial PRIMARY KEY
  );

CREATE TABLE motoqueiro(
  fcpf char(13) REFERENCES funcionario(cpf) UNIQUE,
  cnh  char(9) PRIMARY KEY
  );

CREATE TABLE telefone(
  numero varchar(20) PRIMARY KEY,
  fcpf varchar(11) REFERENCES funcionario(cpf) NOT NULL
  );

CREATE TABLE pedido (
  id serial PRIMARY KEY,
  horario_pedido TIMESTAMP NOT NULL,
  telefone_cliente varchar(20) REFERENCES cliente(telefone) NOT NULL,
  atendente_login varchar(20) REFERENCES atendente(login) NOT NULL,
  entregue_por char(9) REFERENCES motoqueiro(cnh) NOT NULL,
  data_entrega TIMESTAMP
  );
