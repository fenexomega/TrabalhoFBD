 /*criar uma trigger para atualizar o preço total do pedido.*/
 /*para cada novo item de pedido*/

\c deliverydb

CREATE OR REPLACE FUNCTION calcular_valor_gasto_adic() RETURNS TRIGGER
AS $$
DECLARE
  total decimal(10,2);
BEGIN
  total := (SELECT valor_total FROM pedido WHERE id = NEW.pedido_id);
  total := total + (SELECT valor*NEW.qtd FROM prato WHERE codigo = NEW.prato_codigo);
  UPDATE pedido SET valor_total = total WHERE id = NEW.pedido_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_valor_total_adic
AFTER INSERT ON item_pedido
FOR EACH ROW
EXECUTE PROCEDURE calcular_valor_gasto_adic();

CREATE OR REPLACE FUNCTION calcular_valor_gasto_sub() RETURNS TRIGGER
AS $$
DECLARE
  total decimal(10,2);
BEGIN
  total := (SELECT valor_total FROM pedido WHERE id = OLD.pedido_id);
  total := total - (SELECT valor*OLD.qtd FROM prato WHERE codigo = OLD.prato_codigo);
  UPDATE pedido SET valor_total = total WHERE id = OLD.pedido_id;
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_valor_total_sub
BEFORE DELETE ON item_pedido
FOR EACH ROW
EXECUTE PROCEDURE calcular_valor_gasto_sub();



CREATE OR REPLACE FUNCTION timestamp_no_pedido() RETURNS TRIGGER
AS $$
DECLARE
  total decimal(10,2);
BEGIN
  if NEW.horario_pedido IS NULL
  THEN
  update pedido set horario_pedido = now() WHERE id = NEW.id;
  END if;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER horario_do_pedido
AFTER INSERT ON pedido
FOR EACH ROW
EXECUTE PROCEDURE timestamp_no_pedido();


/* ITEMS DO PEDIDO */
CREATE OR REPLACE FUNCTION pegar_items_do_pedido(pd_id int) RETURNS TABLE (pedido_id int, prato_codigo int, qtd int)
AS $$
BEGIN
RETURN QUERY EXECUTE
'SELECT it.pedido_id,pt.codigo ,it.qtd
FROM prato pt, item_pedido it
WHERE it.pedido_id = ' || pd_id || '  AND pt.codigo = it.prato_codigo  ';
END;
$$ LANGUAGE plpgsql;

/*OS PRODUTOS MAIS PEDIDOS DO CLIENTE*/
CREATE OR REPLACE FUNCTION mais_pedidos_cliente(cliente_tel varchar(20)) RETURNS TABLE (cod int,  nome varchar(200), qtd bigint)
AS $$
BEGIN
RETURN QUERY EXECUTE
'SELECT pct.codigo,pct.prato,pct.qtd
FROM
(SELECT pt.nome AS prato, pt.codigo AS codigo, c.telefone, count(*) AS qtd
FROM prato pt, item_pedido ip JOIN pedido p ON
ip.pedido_id = p.id RIGHT JOIN cliente c ON p.telefone_cliente = c.telefone
WHERE pt.codigo = ip.prato_codigo GROUP BY pt.nome,pt.codigo,c.telefone) pct
WHERE pct.telefone = '|| cliente_tel ||'::varchar(20) ORDER BY qtd DESC LIMIT 5';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualizar_item_pedido(pd_id int, pt_cdg int , new_qtd int) RETURNS VOID
AS $$
BEGIN
UPDATE item_pedido SET qtd = new_qtd WHERE pedido_id = pd_id AND prato_codigo = pt_cdg;
RETURN;
END;
$$ LANGUAGE plpgsql;
