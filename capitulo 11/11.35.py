##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.35.py
# Descrição:
##############################################################################

import sqlite3

with sqlite3.connect("brasil.db") as conexão:
    conexão.row_factory = sqlite3.Row
    print(f"{'Id':3s} {'Estado':-20s} {'População':12s}")
    print("=" * 37)
    for estado in conexão.execute("select * from estados order by nome"):
        print(f"{estado['id']:3d} {estado['nome']:-20s} {estado['população']:12d}")
