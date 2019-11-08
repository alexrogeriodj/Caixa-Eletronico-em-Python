##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.20 - Programa 11.5 - Consulta utilizando parâmetros.py
# Descrição:  Programa 11.5 - Consulta utilizando parâmetros
##############################################################################

# Programa 11.5 - Consulta utilizando parâmetros
import sqlite3
from contextlib import closing
nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute('select * from agenda where nome = ?', (nome,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            x += 1
