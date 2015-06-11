 /*criar uma trigger para atualizar o preço total do pedido.*/
 /*para cada novo item de pedido*/

\c deliverydb

CREATE OR REPLACE FUNCTION calcular_valor_gasto() RETURNS TRIGGER
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

CREATE TRIGGER update_valor_total
AFTER INSERT ON item_pedido
FOR EACH ROW
EXECUTE PROCEDURE calcular_valor_gasto();

CREATE OR REPLACE FUNCTION pegar_items_do_pedido(pd_id int) RETURNS TABLE (cod int, nome varchar(200), qtd int, valor decimal(10,2))
AS $$
BEGIN
RETURN QUERY EXECUTE
'SELECT pt.codigo,pt.nome,it.qtd, pt.valor*it.qtd
FROM prato pt, item_pedido it
WHERE it.pedido_id = ' || pd_id || '  AND pt.codigo = it.prato_codigo  ';
END;
$$ LANGUAGE plpgsql;

/*TODO OS PRODUTOS MAIS PEDIDOS DO CLIENTE*/

CREATE OR REPLACE FUNCTION atualizar_item_pedido(pd_id int, pt_cdg int , new_qtd int) RETURNS VOID
AS $$
BEGIN
UPDATE item_pedido SET qtd = new_qtd WHERE pedido_id = pd_id AND prato_codigo = pt_cdg;
RETURN;
END;
$$ LANGUAGE plpgsql;
