##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.14 - Programa 9.7 Criação de uma página inicial em Python.py
# Descrição:  Programa 9.7 Criação de uma página inicial em Python
##############################################################################

# Programa 9.7 Criação de uma página inicial em Python
with open("página.html", "w", encoding="utf-8") as página:
    página.write("<!DOCTYPE html>\n")
    página.write("<html lang=\"pt-BR\">\n")
    página.write("<head>\n")
    página.write("<meta charset=\"utf-8\">\n")
    página.write("<title>Título da Página</title>\n")
    página.write("</head>\n")
    página.write("<body>\n")
    página.write("Olá!")
    for l in range(10):
        página.write(f"<p>{l}</p>\n")
    página.write("</body>\n")
    página.write("</html>\n")
