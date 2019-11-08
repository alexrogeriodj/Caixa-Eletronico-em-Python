##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.31 - Programa 8.13 – Configuração de funções com funções.py
# Descrição:  Programa 8.13 – Configuração de funções com funções
##############################################################################


# Programa 8.13 – Configuração de funções com funções
def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)


def imprime_elemento(e):
    print(f"Valor: {e}")


def épar(x):
    return x % 2 == 0


def éimpar(x):
    return not épar(x)


L = [1, 7, 9, 2, 11, 0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)
