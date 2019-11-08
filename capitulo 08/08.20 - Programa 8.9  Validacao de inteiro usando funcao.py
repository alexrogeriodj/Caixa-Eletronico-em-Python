##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.20 - Programa 8.9 – Validação de inteiro usando função.py
# Descrição:  Programa 8.9 – Validação de inteiro usando função
##############################################################################


# Programa 8.9 – Validação de inteiro usando função
def faixa_int(pergunta, mínimo, máximo):
    while True:
        v = int(input(pergunta))
        if v < mínimo or v > máximo:
            print(f"Valor inválido. Digite um valor entre {mínimo} e {máximo}")
        else:
            return v
