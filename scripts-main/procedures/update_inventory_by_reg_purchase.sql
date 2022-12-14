
CREATE OR REPLACE PROCEDURE 
	public.update_inventory_in_purchase(
		id_reg_purchase NUMERIC
	)
language plpgsql    
as $$
begin
	
	UPDATE product SET
		stock_quantaty = dados.qtde
	FROM 
		item_purchase
	INNER JOIN
		(
			SELECT
				reg_purchase.id as id_purchase,
				item_purchase2.fk_product_id as product_id,
				item_purchase2.unit_price as unit_price,
				(product2.stock_quantaty + item_purchase.quantity) as qtde
			FROM 
				reg_purchase
			INNER JOIN item_purchase item_purchase2 ON item_purchase2.fk_reg_purchase_id = reg_purchase.id
			INNER JOIN product product2 ON product2.id = item_purchase2.fk_product_id
		) as dados ON dados.id_purchase = id_reg_purchase
	
	WHERE
		item_purchase.fk_product_id = product.id
		AND dados.product_id = product.id
		and dados.id_purchase = id_reg_purchase;
	
    commit;
end;$$