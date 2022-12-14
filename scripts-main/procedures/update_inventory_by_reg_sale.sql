
CREATE OR REPLACE PROCEDURE 
	public.update_inventory_in_sale(
		id_reg_sale NUMERIC
	)
language plpgsql    
as $$
begin
	
	UPDATE product SET
		stock_quantaty = dados.qtde
	FROM 
		item_sale
	INNER JOIN
		(
			SELECT
				reg_sale.id as id_sale,
				item_sale2.fk_product_id as product_id,
				item_sale2.unit_price as unit_price,
				(product2.stock_quantaty - item_sale2.quantity) as qtde
			FROM 
				reg_sale
			INNER JOIN item_sale item_sale2 ON item_sale2.fk_reg_sale_id = reg_sale.id
			INNER JOIN product product2 ON product2.id = item_sale2.fk_product_id
		) as dados ON dados.id_sale = id_reg_sale
	
	WHERE
		item_sale.fk_product_id = product.id
		AND dados.product_id = product.id
		and dados.id_sale = id_reg_sale;
	
    commit;
end;$$