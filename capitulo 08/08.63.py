##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.63.py
# Descrição:
##############################################################################

import types


def diz_o_tipo(a):
    tipo = type(a)
    if isinstance(tipo, str):
        return "String"
    elif isinstance(tipo, list):
        return "Lista"
    elif isinstance(tipo, dict):
        return "Dicionário"
    elif isinstance(tipo, int):
        return "Número inteiro"
    elif isinstance(tipo, float):
        return "Número decimal"
    elif isinstance(tipo, types.FunctionType):
        return "Função"
    elif isinstance(tipo, types.BuiltinFunctionType):
        return "Função interna"
    else:
        return str(tipo)


print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1, 2, 3]))
print(diz_o_tipo({"a": 1, "b": 50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))
