-- view para visualizar total de vendas no dia
CREATE OR REPLACE VIEW view_sold_by_date as 

SELECT 
	reg_sale.date,
	SUM(reg_sale.amount)
FROM
	reg_sale
GROUP BY
	reg_sale.date