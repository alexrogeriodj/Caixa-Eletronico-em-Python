##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 03\03.19.py
# Descrição:
##############################################################################

nome = "João"
idade = 22
grana = 51.34
"%s tem %d anos e R$%f no bolso." % (nome, idade, grana)
"%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana)
"%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana)
"%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana)
