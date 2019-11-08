##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.43.py
# Descrição:
##############################################################################

import sqlite3
print("Região Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
            select região, count(*)
            from estados
            group by região"""):
        print("{0:6} {1:17}".format(*região))
