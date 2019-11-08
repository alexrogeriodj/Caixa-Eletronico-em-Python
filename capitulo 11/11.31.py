##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.31.py
# Descrição:
##############################################################################

import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    conexão.row_factory = sqlite3.Row
    with closing(conexão.cursor()) as cursor:
        for registro in cursor.execute("select * from agenda"):
            print(f"Nome: {registro['nome']}\nTelefone: {registro['telefone']}")
