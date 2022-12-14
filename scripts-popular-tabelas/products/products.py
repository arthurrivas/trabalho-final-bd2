product = [
    # tem 10 lotr
    {
        'id': 1,
        'stock_quantity': 10,
        "default_sale_price": 150.00,
        "last_sale": '2021-08-05T00:00:00',
        "last_puchase": '2021-02-02T00:00:00',
        "fk_book_id": 1,
    },
    # tem 5 hobbit
    {
        'id': 2,
        'stock_quantity': 5,
        "default_sale_price": 50.00,
        "last_sale": '2021-08-01T00:00:00',
        "last_puchase": '2020-05-09T00:00:00',
        "fk_book_id": 2,
    },
    # tem 3 pequeno principe
    {
        'id': 3,
        'stock_quantity': 3,
        "default_sale_price": 15.00,
        "last_sale": '2017-08-01T00:00:00',
        "last_puchase": '2015-04-09T00:00:00',
        "fk_book_id": 3,
    },
    # tem 2 iluminado
    {
        'id': 4,
        'stock_quantity': 2,
        "default_sale_price": 49.90,
        "last_sale": '2018-08-01T00:00:00',
        "last_puchase": '2017-07-04T00:00:00',
        "fk_book_id": 4,
    },
    # tem 1 nome do vento
    {
        'id': 5,
        'stock_quantity': 1,
        "default_sale_price": 74.00,
        "last_sale": '2000-08-07T00:00:00',
        "last_puchase": '2000-05-05T00:00:00',
        "fk_book_id": 5,
    },
    # tem 1 homens e monstros
    {
        'id': 6,
        'stock_quantity': 1,
        "default_sale_price": 15.99,
        "last_sale": '2021-08-01T00:00:00',
        "last_puchase": '2020-05-05T00:00:00',
        "fk_book_id": 6,
    },
    # tem 3 alice no pais das maravilhas
    {
        'id': 7,
        'stock_quantity': 3,
        "default_sale_price": 59.00,
        "last_sale": '2021-08-08T00:00:00',
        "last_puchase": '2021-04-04T00:00:00',
        "fk_book_id": 7,
    },
    # tem 7 dracula
    {
        'id': 8,
        'stock_quantity': 7,
        "default_sale_price": 89.00,
        "last_sale": '2022-02-02T00:00:00',
        "last_puchase": '2021-08-01T00:00:00',
        "fk_book_id": 8,
    },
    # tem 1 dinastia americana
    {
        'id': 9,
        'stock_quantity': 1,
        "default_sale_price": 25.00,
        "last_sale": '2020-08-01T00:00:00',
        "last_puchase": '2019-04-04T00:00:00',
        "fk_book_id": 9,
    },
    # tem 8 joyland
    {
        'id': 10,
        'stock_quantity': 8,
        "default_sale_price": 88.00,
        "last_sale": '2022-02-02T00:00:00',
        "last_puchase": '2021-01-01T00:00:00',
        "fk_book_id": 10,
    },

    # tem 28 it
    {
        'id': 11,
        'stock_quantity': 28,
        "default_sale_price": 55.00,
        "last_sale": '2020-08-01T00:00:00',
        "last_puchase": '2019-08-01T00:00:00',
        "fk_book_id": 11,
    },
    # tem 10 harry potter e o enigma do príncipe
    {
        'id': 12,
        'stock_quantity': 10,
        "default_sale_price": 45.00,
        "last_sale": '2021-08-05T00:00:00',
        "last_puchase": '2020-05-01T00:00:00',
        "fk_book_id": 12,
    },
    # tem 6 harry potter e a pedra filosofal
    {
        'id': 13,
        'stock_quantity': 6,
        "default_sale_price": 44.00,
        "last_sale": '2018-07-07T00:00:00',
        "last_puchase": '2015-08-01T00:00:00',
        "fk_book_id": 13,
    },
    # tem 4 harry potter e a câmara secreta
    {
        'id': 14,
        'stock_quantity': 4,
        "default_sale_price": 38.00,
        "last_sale": '2021-08-05T00:00:00',
        "last_puchase": '2020-05-01T00:00:00',
        "fk_book_id": 14,
    },
    # tem 10 harry potter e o prisioneiro de azkaban
    {
        'id': 15,
        'stock_quantity': 10,
        "default_sale_price": 25.00,
        "last_sale": '2021-08-05T00:00:00',
        "last_puchase": '2020-05-01T00:00:00',
        "fk_book_id": 15,
    },
    # tem 7 harry potter e o cálice de fogo
    {
        'id': 16,
        'stock_quantity': 7,
        "default_sale_price": 40.00,
        "last_sale": '2022-05-04T00:00:00',
        "last_puchase": '2020-08-01T00:00:00',
        "fk_book_id": 16,
    },
    # tem 18 harry potter e a ordem da fênix
    {
        'id': 17,
        'stock_quantity': 18,
        "default_sale_price": 30.00,
        "last_sale": '2022-05-01T00:00:00',
        "last_puchase": '2021-02-02T00:00:00',
        "fk_book_id": 17,
    },
    # tem 15 harry potter e as reliquias da morte
    {
        'id': 18,
        'stock_quantity': 15,
        "default_sale_price": 28.50,
        "last_sale": '2020-08-01T00:00:00',
        "last_puchase": '2019-08-01T00:00:00',
        "fk_book_id": 18,
    },

]



with open('product.txt', 'w') as f:
    for item in product:
        f.write(f"""
           INSERT INTO public.product(
            id, stock_quantaty, default_sale_price, last_sale, last_puchase, fk_book_id)
            VALUES (
                {item.get('id')}, 
                {item.get('stock_quantity')}, 
                {item.get('default_sale_price')}, 
                '{item.get('last_sale')}', 
                '{item.get('last_puchase')}', 
                {item.get('fk_book_id')});
        """)

        f.write('\n')
