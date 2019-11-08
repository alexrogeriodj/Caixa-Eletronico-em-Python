##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 10\10.32.py
# Descrição:
##############################################################################


class Telefone:
    def __init__(self, número, tipo=None):
        self.número = número
        self.tipo = tipo

    def __str__(self):
        if self.tipo is not None:
            tipo = self.tipo
        else:
            tipo = ""
        return f"{self.número} {tipo}"

    def __eq__(self, outro):
        return self.número == outro.número and (
               (self.tipo == outro.tipo) or (
                self.tipo is None or outro.tipo is None))

    @property
    def número(self):
        return self.__número

    @número.setter
    def número(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__número = valor
