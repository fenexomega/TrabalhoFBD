
\c deliverydb
/*TODO CRIAR VIEW PARA VER OS MAIS PEDIDOS*/



create or replace view pedidos_com_nomes as
select p.id,p.horario_pedido,
c.nome as Cliente ,
p.atendente_login,
fm.nome as Entregador,
p.valor_total
from pedido p
inner join cliente c
on p.telefone_cliente = c.telefone
inner join motoqueiro m
on m.cnh = p.entregue_por
inner join funcionario fm
on m.fcpf = fm.cpf
order by p.horario_pedido DESC;

CREATE OR REPLACE VIEW motoqueiro_com_nome AS
SELECT f.id,f.nome,m.cnh
FROM motoqueiro m
JOIN funcionario f
ON f.cpf = m.fcpf
GROUP BY f.id,f.nome,m.cnh
ORDER BY f.id ;
