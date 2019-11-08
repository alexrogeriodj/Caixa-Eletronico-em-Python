##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.16 - Programa 8.6 – Função modificada para facilitar o rastreamento.py
# Descrição:  Programa 8.6 – Função modificada para facilitar o rastreamento
##############################################################################


# Programa 8.6 – Função modificada para facilitar o rastreamento
def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f" fatorial de {n} = {fat}")
    return fat


fatorial(4)
