##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 10\10.23.py
# Descrição:
##############################################################################

from functools import total_ordering


@total_ordering
class Nome:
    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = Nome.CriaChave(nome)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome } Chave: { self.chave }>"

    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()
