author = [
    # hobbit, lotr
    {
        'id': 1,
        'name': "j.r.r tolkien",
        'email': "tolkien@hotmail.com",
    },
    # dinastia americana
    {
        'id': 2,
        'name': "tracey livesay",
        'email': "livesay@outlook.com",
    },
    # pequeno principe
    {
        'id': 3,
        'name': "antoine de saint-exupéry",
        'email': "antoine@gmail.com",
    },
    # o iluminado, joyland e it
    {
        'id': 4,
        'name': "stephen king",
        'email': "stephen@outlook.com",
    },
    # o nome do vento
    {
        'id': 5,
        'name': "patrick rothfuss",
        'email': "rothfuss@hotmail.com",
    },
    # homens e monstros
    {
        'id': 6,
        'name': "patrick ness",
        'email': "ness@outlook.com",
    },
    # alice no pais das maravilhas
    {
        'id': 7,
        'name': "lewis carroll",
        'email': "",
    },
    # dracula
    {
        'id': 8,
        'name': "bram stoker",
        'email': "",
    },
    # harry potter e o enigma do príncipe, reliquias da morte, ordem da fenix,
    # prisioneiro de azkaban, camara secreta, pedra filosofal, calice de fogo
    {
        'id': 9,
        'name': "j.k rowling",
        'email': "rowling@gmail.com",
    },
]



with open('autores.txt', 'w') as f:
    for item in author:
        f.write(f"""
            INSERT INTO public.author(
            id, name, email)
            VALUES (
                {item.get('id')}, 
                '{item.get('name')}', 
                '{item.get('email')}');
        """)