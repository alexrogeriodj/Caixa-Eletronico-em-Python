##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.14.py
# Descrição:
##############################################################################

a = 5


def muda_e_imprime():
    global a
    a = 7
    print(f"A dentro da função: {a}")


print(f"a antes de mudar: {a}")
muda_e_imprime()
print(f"a depois de mudar: {a}")
