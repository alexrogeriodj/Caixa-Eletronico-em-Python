##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.25 - Programa 11.6 - Exemplo de update sem where e com rowcount.py
# Descrição:  Programa 11.6 - Exemplo de update sem where e com rowcount
##############################################################################

# Programa 11.6 - Exemplo de update sem where e com rowcount
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""update agenda
                             set telefone = '12345-6789' """)
        print("Registros alterados: ", cursor.rowcount)
