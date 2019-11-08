##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.34 - Programa 8.14 – Função soma com número indeterminado de parâmetros.py
# Descrição:  Programa 8.14 – Função soma com número indeterminado de parâmetros
##############################################################################


# Programa 8.14 – Função soma com número indeterminado de parâmetros
def soma(*args):
    s = 0
    for x in args:
        s += x
    return s


soma(1, 2)
soma(2)
soma(5, 6, 7, 8)
soma(9, 10, 20, 30, 40)
