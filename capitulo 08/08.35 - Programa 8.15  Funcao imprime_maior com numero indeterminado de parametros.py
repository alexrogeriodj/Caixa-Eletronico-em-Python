##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.35 - Programa 8.15 – Função imprime_maior com número indeterminado de parâmetros.py
# Descrição:  Programa 8.15 – Função imprime_maior com número indeterminado de parâmetros
##############################################################################


# Programa 8.15 – Função imprime_maior com número indeterminado de parâmetros
def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)


imprime_maior("Maior:", 5, 4, 3, 1)
imprime_maior("Max:", *[1, 7, 9])
