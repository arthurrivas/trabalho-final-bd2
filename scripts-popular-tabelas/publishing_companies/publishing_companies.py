publishing_companies = [
    # harry potter e o enigma do príncipe, reliquias da morte, ordem da fenix,
    # prisioneiro de azkaban, camara secreta, pedra filosofal, calice de fogo
    {
        'id': 1,
        'name': "Rocco",
        'cnpj': '12348678900234',
        'url_site': 'https://www.rocco.com.br/'
    },
    # dracula e alice no pais das maravilhas
    {
        'id': 2,
        'name': "darkside",
        'cnpj': '82385978908235',
        'url_site': 'https://www.darksidebooks.com.br/'
    },
    # dinastia americana e homens e monstros
    {
        'id': 3,
        'name': "intrinseca",
        'cnpj': '11395978909296',
        'url_site': 'https://www.intrinseca.com.br/'
    },
    # hobbit, pequeno principe e lotr
    {
        'id': 4,
        'name': "harperCollins",
        'cnpj': '12444611911239',
        'url_site': 'https://harpercollins.com.br/'
    },
    # joyland, it e o iluminado
    {
        'id': 5,
        'name': "suma",
        'cnpj': '12341618911214',
        'url_site': ''
    },
    # o nome do vento
    {
        'id': 6,
        'name': "arqueiro",
        'cnpj': '12341618911214',
        'url_site': 'https://www.editoraarqueiro.com.br/'
    }

]


with open('publishing_companies.txt', 'w') as f:
    for item in publishing_companies:
        f.write(f"""
            INSERT INTO public.publishing_company(
            id, name, cnpj, url_site)
            VALUES (
                {item.get('id')}, 
                '{item.get('name')}', 
                '{item.get('cnpj')}', 
                '{item.get('url_site')}');

        """)

        f.write('\n')
