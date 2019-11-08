##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 10\10.01.py
# Descrição:
##############################################################################


class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2


tv = Televisão()
tv.ligada
tv.canal
tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 4
tv.canal
tv_sala.canal
