##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.08.py
# Descrição:
##############################################################################

import sqlite3
dados = [("João",  "98901-0109"),
         ("André", "98902-8900"),
         ("Maria", "97891-3321")]
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.executemany('''
      insert into agenda (nome, telefone)
      values(?, ?)
      ''', dados)
conexão.commit()
cursor.close()
conexão.close()
