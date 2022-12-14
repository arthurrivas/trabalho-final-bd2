book = [
    {
        'id': 1,
        'title': "o senhor dos anéis",
        'description': "livro sobre um anel",
    },
    {
        'id': 2,
        'title': "o hobbit",
        'description': "uma aventura na terra media",
    },
    {
        'id': 3,
        'title': "o pequeno principe",
        'description': "livro sobre um pequeno principe",
    },
    {
        'id': 4,
        'title': "o iluminado",
        'description': "livro sobre um maluco",
    },
    {
        'id': 5,
        'title': "o nome do vento",
        'description': "livro sobre um nome do vento",
    },
    {
        'id': 6,
        'title': "homens e monstros",
        'description': "livro sobre homens e monstros",
    },
    {
        'id': 7,
        'title': "alice no pais das maravilhas",
        'description': "livro sobre uma garota que cai em um buraco",
    },
    {
        'id': 8,
        'title': "dracula",
        'description': "livro sobre um vampiro",
    },
    {
        'id': 9,
        'title': "dinastia americana",
        'description': "livro sobre uma dinastia americana",
    },
    {
        'id': 10,
        'title': "joyland",
        'description': "livro sobre um parque de diversoes",
    },
    {
        'id': 11,
        'title': "it",
        'description': "livro sobre um palhaço",
    },
    {
        'id': 12,
        'title': "harry potter e o enigma do príncipe",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 13,
        'title': "harry potter e a pedra filosofal",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 14,
        'title': "harry potter e a câmara secreta",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 15,
        'title': "harry potter e o prisioneiro de azkaban",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 16,
        'title': "harry potter e o cálice de fogo",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 17,
        'title': "harry potter e a ordem da fênix",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
    {
        'id': 18,
        'title': "harry potter e as relíquias da morte",
        'description': "livro sobre um garoto que vai a escola de magia",
    },
]



with open('book.txt', 'w') as f:
    for item in book:
        f.write(f"""
           INSERT INTO public.book(
            id, title, description)
            VALUES (
                {item.get('id')}, 
                '{item.get('title')}', 
                '{item.get('description')}');
        """)

        f.write('\n')

