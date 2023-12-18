# PEP8 OK
# -*- coding: utf-8 -*-

from datetime import datetime

"""Cálculo de idade simples, utilizando input e datetime
"""
    
ano_nasc = int(input('Ano que você nasceu '))
mes_nasc = int(input('Mês que você nasceu '))
dia_nasc = int(input('Dia que você nasceu '))

data_nasc = datetime(ano_nasc, mes_nasc, dia_nasc)
data_atual = datetime.now()

diff = data_atual - data_nasc

dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias.')
