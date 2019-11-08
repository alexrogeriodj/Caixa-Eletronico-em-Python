##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.82.py
# Descrição:
##############################################################################

[x for x in range(10) if x % 3 == 0]
(x for x in range(10) if x % 3 == 0)
for y in (x for x in range(10) if x % 3 == 0):
    print(y)
