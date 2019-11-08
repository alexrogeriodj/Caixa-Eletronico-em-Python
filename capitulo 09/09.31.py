##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.31.py
# Descrição:
##############################################################################

import time
agora = time.localtime()
print(f"Ano: {agora.tm_year}")
print(f"Mês: {agora.tm_mon}")
print(f"Dia: {agora.tm_mday}")
print(f"Hora: {agora.tm_hour}")
print(f"Minuto: {agora.tm_min}")
print(f"Segundo: {agora.tm_sec}")
print(f"Dia da semana: {agora.tm_wday}")
print(f"Dia no ano: {agora.tm_yday}")
print(f"Horário de verão: {agora.tm_isdst}")
