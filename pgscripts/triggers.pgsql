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
