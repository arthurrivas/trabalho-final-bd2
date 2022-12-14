CREATE OR REPLACE FUNCTION update_total_value_reg_purchase
	(
		id_reg_purchase INTEGER
	) RETURNS SETOF RECORD AS $$
BEGIN

	UPDATE reg_purchase set 
		amount = dados.total_value
	from (
		SELECT
			SUM((item_purchase.unit_price * item_purchase.quantity)) as total_value
		from
			item_purchase
		WHERE item_purchase.fk_reg_purchase_id = id_reg_purchase
	
	) as dados 
	WHERE 
		reg_purchase.id = id_reg_purchase;

					 
	RETURN QUERY
		SELECT 
			* 
		FROM 
			reg_purchase 
		WHERE 
			reg_purchase.id = id_reg_purchase;
	RETURN;
			
						
END;

$$ LANGUAGE plpgsql;

-- CALL FUNCTION
-- SELECT * FROM update_total_value_reg_purchase(1) as (id INTEGER, data DATE, amount DOUBLE PRECISION, id_company INTEGER)