
-- ANTES DE INSERIR UM REGISTRO NA TABELA DE ITEM_SALE< VERIFICA SE O PRODUTO TEM EM STOCK
CREATE TRIGGER t_update_stock
BEFORE INSERT ON item_sale
FOR EACH ROW
EXECUTE PROCEDURE update_stock_on_sale();

CREATE OR REPLACE FUNCTION update_stock_on_sale() RETURNS TRIGGER
AS
$$
DECLARE
	qtd integer; -- quantidade produto em estoque
BEGIN

	Select 
		stock_quantaty 
	from 
		product 
	where 
		id = NEW.id into qtd;

	IF qtd < NEW.quantity then
		raise exception 'Quantidade indisponivel em estoque.';
	ELSE
		UPDATE product SET stock_quantaty = stock_quantaty - NEW.quantity
			WHERE id = NEW.id;
	END IF;
	return NEW;
END
$$ LANGUAGE plpgsql;

