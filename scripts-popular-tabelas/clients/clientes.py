clientes = [
    {
        'id': 1,
        'name': "arthur",
        'cpf': '12345678901',
        'email': 'arthur@gmail.com',
        'birthday': '2000-07-19T00:00:00'
    },
    {
        'id': 2,
        'name': "joao",
        'cpf': '12345678902',
        'email': 'joao@hotmail.com',
        'birthday': '2000-04-17T00:00:00'
    },
    {
        'id': 3,
        'name': "maria",
        'cpf': '12398745603',
        'email': 'maria@outlook.com',
        'birthday': '2000-01-01T00:00:00'
    },
    {
        'id': 4,
        'name': "jose",
        'cpf': '15948726310',
        'email': 'jose@outlook.com',
        'birthday': '2000-01-01T00:00:00'
    },
    {
        'id': 5,
        'name': "nathalia",
        'cpf': '26378986701',
        'email': '',
        'birthday': '2000-08-01T00:00:00'
    },
    {
        'id': 6,
        'name': "roberto",
        'cpf': '28378216501',
        'email': '',
        'birthday': '2000-08-01T00:00:00'
    },
]

with open('clients.txt', 'w') as f:
    for item in clientes:
        f.write(f"""
        INSERT INTO public.client(
            id, name, cpf, email, birthday)
            VALUES (
                {item.get('id')}, 
                '{item.get('name')}',
                '{item.get('cpf')}', 
                '{item.get('email')}', 
                '{item.get('birthday')}');
        """)

        f.write('\n')




