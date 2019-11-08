##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.54 - Programa 8.18 – Módulo entrada (entrada.py).py
# Descrição:  Programa 8.18 – Módulo entrada (entrada.py)
##############################################################################


# Programa 8.18 – Módulo entrada (entrada.py)
def valida_inteiro(mensagem, mínimo, máximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print(f"Digite um valor entre {mínimo} e {máximo}")
        except ValueError:
            print("Você deve digitar um número inteiro")
