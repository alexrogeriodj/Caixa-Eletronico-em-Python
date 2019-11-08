##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 10\10.39.py
# Descrição:
##############################################################################


class EstoqueException(Exception):
    def __init__(self, mensagem, codigo_de_erro):
        super().__init__(mensagem)
        self.codigo_de_erro = codigo_de_erro


def verifique_quantidade(quantidade):
    if quantidade < 0:
        raise EstoqueException("Quantidade negativa", codigo_de_erro=1)


try:
    verifique_quantidade(-10)
except EstoqueException as ee:
    print(f"Erro: {ee.codigo_de_erro} {ee}")
