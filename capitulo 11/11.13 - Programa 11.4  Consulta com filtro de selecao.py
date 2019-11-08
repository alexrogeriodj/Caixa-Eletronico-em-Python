##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.13 - Programa 11.4 – Consulta com filtro de seleção.py
# Descrição:  Programa 11.4 – Consulta com filtro de seleção
##############################################################################

# Programa 11.4 – Consulta com filtro de seleção
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = 'Nilo'")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
