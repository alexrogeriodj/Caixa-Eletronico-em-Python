##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.53.py
# Descrição:
##############################################################################

import sqlite3
feriados = [["2018-01-01", "Confraternização Universal"],
            ["2018-04-21", "Tiradentes"],
            ["2018-05-01", "Dia do trabalhador"],
            ["2018-09-07", "Independência"],
            ["2018-10-12", "Padroeira do Brasil"],
            ["2018-11-02", "Finados"],
            ["2018-11-15", "Proclamação da República"],
            ["2018-12-25", "Natal"]]
with sqlite3.connect("brasil.db") as conexão:
    conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
    conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)
