##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 11\11.41.py
# Descrição:
##############################################################################

import sqlite3
dados = [["SP", "SE", "São Paulo"],
         ["MG", "SE", "Minas Gerais"],
         ["RJ", "SE", "Rio de Janeiro"],
         ["BA", "NE", "Bahia"],
         ["RS", "S", "Rio Grande do Sul"],
         ["PR", "S", "Paraná"],
         ["PE", "NE", "Pernambuco"],
         ["CE", "NE", "Ceará"],
         ["PA", "N", "Pará"],
         ["MA", "NE", "Maranhão"],
         ["SC", "S", "Santa Catarina"],
         ["GO", "CO", "Goiás"],
         ["PB", "NE", "Paraíba"],
         ["ES", "SE", "Espírito Santo"],
         ["AM", "N", "Amazonas"],
         ["RN", "NE", "Rio Grande do Norte"],
         ["AL", "NE", "Alagoas"],
         ["PI", "NE", "Piauí"],
         ["MT", "CO", "Mato Grosso"],
         ["DF", "CO", "Distrito Federal"],
         ["MS", "CO", "Mato Grosso do Sul"],
         ["SE", "NE", "Sergipe"],
         ["RO", "N", "Rondônia"],
         ["TO", "N", "Tocantins"],
         ["AC", "N", "Acre"],
         ["AP", "N", "Amapá"],
         ["RR", "N", "Roraima"]]

with sqlite3.connect("brasil.db") as conexão:
    conexão.executemany("""update estados
                           set sigla = ?,
                           região = ?
                           where nome = ?""", dados)
