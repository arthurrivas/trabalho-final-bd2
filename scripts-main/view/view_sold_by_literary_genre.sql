-- view para visualizar total de vendas por genero literario
CREATE OR REPLACE VIEW view_sold_by_literary_genre as 
	
SELECT
	literary_genre."name",
	SUM((item_sale.quantity * item_sale.unit_price))
FROM
	literary_genre
INNER JOIN 
	belongs_to ON belongs_to.fk_literary_genre_id = literary_genre.id
INNER JOIN 
	book ON book.id = belongs_to.fk_book_id
INNER JOIN 
	product ON product.fk_book_id = book.id
INNER JOIN
	item_sale ON item_sale.fk_product_id = product.id
GROUP BY 
	literary_genre."name"

