CREATE USER user_delivery WITH ENCRYPTED PASSWORD 'delivery';
CREATE USER admin_delivery WITH ENCRYPTED PASSWORD 'root';

CREATE DATABASE deliverydb OWNER admin_delivery;
/*conectar ao banco*/
/*GRANT USAGE ON SCHEMA public to user_delivery;*/
/*ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO user_delivery;*/
GRANT CONNECT ON DATABASE deliverydb to user_delivery;
\c deliverydb



CREATE TABLE funcionario (
  id serial,
  cpf char(13) PRIMARY KEY,
  nome varchar(200) NOT NULL,
  salario decimal(10,2) NOT NULL
  );

CREATE TABLE cliente (
  id SERIAL PRIMARY KEY,
  telefone varchar(20) UNIQUE,
  /*aniversario date NOT NULL,*/
  nome varchar(200) NOT NULL,
  rua varchar (200) NOT NULL,
  bairro varchar(100) NOT NULL,
  complemento varchar(500)
  );

CREATE TABLE atendente (
  fcpf char(13) REFERENCES funcionario(cpf) UNIQUE,
  login varchar(20) PRIMARY KEY,
  senha char(32)
  );

CREATE TABLE prato (
  codigo serial PRIMARY KEY,
  nome varchar(200) NOT NULL,
  valor DECIMAL(5,2) NOT NULL
  );

CREATE TABLE motoqueiro(
  fcpf char(13) REFERENCES funcionario(cpf) UNIQUE NOT NULL,
  cnh  char(9) PRIMARY KEY
  );

CREATE TABLE telefone (
  numero varchar(20) PRIMARY KEY,
  fcpf varchar(11) REFERENCES funcionario(cpf) NOT NULL
  );

CREATE TABLE pedido (
  id serial PRIMARY KEY,
  horario_pedido TIMESTAMP UNIQUE,
  telefone_cliente varchar(20) REFERENCES cliente(telefone) NOT NULL,
  atendente_login varchar(20) REFERENCES atendente(login) NOT NULL,
  entregue_por char(9) REFERENCES motoqueiro(cnh) NOT NULL,
  valor_total decimal(10,2) DEFAULT 0.0
  );

CREATE TABLE item_pedido (
  pedido_id serial REFERENCES pedido(id) ,
  prato_codigo serial REFERENCES prato(codigo) ,
  qtd integer,
  PRIMARY KEY (pedido_id,prato_codigo)
  );
