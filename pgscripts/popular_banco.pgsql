\c deliverydb

INSERT INTO funcionario VALUES
('18345820247','Ítalo Lemos',1500.33),
('55711864882','Júlio Vargas',1852.23),
('60554357216','João Carlos',2324.23),
('36202349492','Alex Sandro',1500.96),
('83604173698','Mariana Nascimento',2345.23),
('22468381858','Lula Molusco',2094.34),
('25403227350','Patrick Estrela',3451.34),
('76832941366','Raul Seixas',2345.12),
('91322332304','Daiana Mendes',3562.12),
('18314560871','Jacinto Pinto',1252.54);

INSERT INTO cliente VALUES
('986090381','20/2/1973','Felipe Neto','Rua Francisco Deogracias Reche 732','Borda do Campo',NULL),
('988878842','10/11/1958','PC Siqueira','Rua Valdemar Rodrigues Silva 411','Parque Lanel','Próximo à padaria Pão'),
('993385062','17/7/1974', 'Júlio Pinto','Rua Henrique 431','Parque Lanel',NULL),
('987954924','4/10/1977', 'Patrícia Calado','Rua A 23','Aldeia do Lago',NULL),
('993507735','23/11/1989', 'Lima Barreto','Rua Mar Mediterrâneo 1532','Parque Marinha',NULL),
('997463229','17/9/1960', 'Chico Buarque','Rua Carlos Alberto de Oliveira 2212','Tremembé','AP 14'),
('998949747','9/11/1962', 'Deodoro da Fonseca','Rua Padre Palmeira 442','Vila Dionisia',NULL),
('999099446','4/2/1940', 'Luís Inácio Lula','Rua Nicolau Tolentino de Almeida 900','Vila Dionisia',NULL),
('997735792','1/11/1981', 'Fernando Henrique','Rua Tony (Justinópolis) 123','Aldeia do Lago',NULL),
('985716932','27/3/1942', 'Cardoso','Rua Teodoro dos Reis 345','Aldeia do Lago',NULL);

INSERT INTO atendente VALUES
('18345820247','ilemos','5c2303c01ef71cf05775f96f3de9059c'),
('36202349492','asandro','44fc1a472fa17257f786d8ef405e95e9'),
('60554357216','jcarlos','ced566012a49f76eb2a0f37074735024'),
('55711864882','jvargas','cc73e6f0be487361c1e5a46388541c3a'),
('83604173698','mnascimento','ee52100607c63d1ba2ae1bb15e77aa91');

INSERT INTO telefone VALUES
('807919915','18345820247'),
('934459721','55711864882'),
('833886243','60554357216'),
('856748504','25403227350'),
('844569314','25403227350'),
('811046926','91322332304'),
('865517929','18314560871'),
('934146057','60554357216'),
('911853893','76832941366'),
('873149691','76832941366');

INSERT INTO prato(nome,valor) VALUES
('Espaguete Bolonhesa',30.32),
('Charuto de Uva', 15.10),
('Água com gás', 2.00),
('Sushi de salmão',8.00),
('Lasanha a bolonhesa',25.00),
('Esfiha de queijo',2.00),
('Esfiha de carne',2.00),
('Petit Gateau',7.50),
('Macarrão com camarão',23.52),
('Brownie com Sorvete',8.00),
('Feijão com pão',2.30),
('Canja',3.50);

INSERT INTO motoqueiro VALUES
('22468381858','686827067'),
('25403227350','299679625'),
('76832941366','869174990'),
('91322332304','588474255'),
('18314560871','911629397');

INSERT INTO pedido(horario_pedido,telefone_cliente,atendente_login,entregue_por) VALUES
(TIMESTAMP '2013-09-23 11:34','988878842','asandro','588474255'),
(TIMESTAMP '2013-09-27 11:11','998949747','jcarlos','869174990'),
(TIMESTAMP '2014-03-27 11:22','988878842','mnascimento','686827067'),
(TIMESTAMP '2014-09-27 11:00','988878842','jcarlos','911629397'),
(TIMESTAMP '2015-03-27 11:00','999099446','jvargas','686827067'),
(TIMESTAMP '2015-04-27 11:01','988878842','jvargas','588474255'),
(TIMESTAMP '2015-05-27 11:03','997463229','mnascimento','686827067'),
(TIMESTAMP '2015-05-27 11:03','987954924','ilemos','911629397'),
(TIMESTAMP '2015-05-27 11:03','997463229','ilemos','299679625'),
(TIMESTAMP '2015-05-27 11:03','999099446','mnascimento','869174990');

INSERT INTO item_pedido VALUES
(1,1,1),
(1,3,2),
(2,3,1),
(3,1,1),
(4,4,1),
(4,12,1),
(5,3,2),
(6,3,3),
(7,3,1),
(8,3,1),
(9,3,4),
(10,3,1);