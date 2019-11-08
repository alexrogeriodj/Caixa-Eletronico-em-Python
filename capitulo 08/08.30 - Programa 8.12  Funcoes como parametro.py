##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.30 - Programa 8.12 – Funções como parâmetro.py
# Descrição:  Programa 8.12 – Funções como parâmetro
##############################################################################


# Programa 8.12 – Funções como parâmetro
def soma(a, b):
    return a + b


def subtração(a, b):
    return a - b


def imprime(a, b, foper):
    print(foper(a, b))


imprime(5, 4, soma)
imprime(10, 1, subtração)
