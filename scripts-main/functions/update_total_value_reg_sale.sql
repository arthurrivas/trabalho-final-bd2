CREATE OR REPLACE FUNCTION update_total_value_reg_sale
	(
		id_reg_sale INTEGER
	) RETURNS SETOF RECORD AS $$
BEGIN

	UPDATE reg_sale set 
		amount = dados.total_value
	from (
		SELECT
			SUM((item_sale.unit_price * item_sale.quantity)) as total_value
		from
			item_sale
		WHERE item_sale.fk_reg_sale_id = id_reg_sale
	
	) as dados 
	WHERE 
		reg_sale.id = id_reg_sale;

					 
	RETURN QUERY
		SELECT 
			* 
		FROM 
			reg_sale 
		WHERE 
			reg_sale.id = id_reg_sale;
	RETURN;
			
						
END;

$$ LANGUAGE plpgsql;

-- CALL FUNCTION
-- SELECT * FROM update_total_value_reg_sale(1) as (id INTEGER, data DATE, amount DOUBLE PRECISION, id_client INTEGER)