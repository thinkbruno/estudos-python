# PEP8 OK
# -*- coding: utf-8 -*-

from forex_python.converter import CurrencyRates

c = CurrencyRates()

us_vl = float(input("Valor em Dólar: "))

brl = round(c.convert("USD", "BRL", us_vl), 2)

print(f"R$ {brl}")
