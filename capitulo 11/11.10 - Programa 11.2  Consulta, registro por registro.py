##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.10 - Programa 11.2 – Consulta, registro por registro.py
# Descrição:  Programa 11.2 – Consulta, registro por registro
##############################################################################

# Programa 11.2 – Consulta, registro por registro
import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexão.close()
