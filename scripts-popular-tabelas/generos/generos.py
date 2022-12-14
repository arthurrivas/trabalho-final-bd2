
library_genre = [
    {
        'id': 1,
        'name': "romance",
    },
    {
        'id': 2,
        'name': "ficção",
    },
    {
        'id': 3,
        'name': "terror",
    },
    {
        'id': 4,
        'name': "aventura",
    },
    {
        'id': 5,
        'name': "suspense",
    },
    {
        'id': 6,
        'name': "infantil",
    },
]


with open('generos.txt', 'w') as f:
    for item in library_genre:
        f.write(f"""
            INSERT INTO public.literary_genre(
            id, name)
            VALUES (
                {item.get('id')}, 
                '{item.get('name')}');
        """)

        f.write('\n')


