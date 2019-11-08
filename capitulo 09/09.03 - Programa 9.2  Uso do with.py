##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.03 - Programa 9.2 – Uso do with.py
# Descrição:  Programa 9.2 – Uso do with
##############################################################################

# Programa 9.2 – Uso do with
with open("números.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
