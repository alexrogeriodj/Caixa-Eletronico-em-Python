##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.09 - Programa 11.1 - Consulta com múltiplos resultados.py
# Descrição:  Programa 11.1 - Consulta com múltiplos resultados
##############################################################################

# Programa 11.1 - Consulta com múltiplos resultados
import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()
for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")
cursor.close()
conexão.close()
