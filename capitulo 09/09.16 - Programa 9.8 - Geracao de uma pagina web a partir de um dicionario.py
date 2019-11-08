##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.16 - Programa 9.8 - Geração de uma página web a partir de um dicionário.py
# Descrição:  Programa 9.8 - Geração de uma página web a partir de um dicionário
##############################################################################

# Programa 9.8 - Geração de uma página web a partir de um dicionário
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("filmes.html", "w", encoding="utf-8") as página:
    página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
    for c, v in filmes.items():
        página.write(f"<h1>{c}</h1>\n")
        for e in v:
            página.write(f"<h2>{e}</h2>\n")
    página.write("</body></html>")
