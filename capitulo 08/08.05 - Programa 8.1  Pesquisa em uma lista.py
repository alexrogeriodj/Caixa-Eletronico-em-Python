##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.05 - Programa 8.1 – Pesquisa em uma lista.py
# Descrição:  Programa 8.1 – Pesquisa em uma lista
##############################################################################


# Programa 8.1 – Pesquisa em uma lista
def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
