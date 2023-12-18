# PEP8 OK
# -*- coding: utf-8 -*-

import phonenumbers
from phonenumbers import carrier, geocoder

"""descobrindo operadora e local de um número de celular (pode ser que em casos de portabilidade a api aponte a operadora antiga)
"""

mobile = input("Digite seu celular com DDD (Somente números): ")

phoneNumber = phonenumbers.parse(f"+55{mobile}")

__carrier = carrier.name_for_number(phoneNumber, 'pt-br')
__region = geocoder.description_for_number(phoneNumber, 'pt-br')

print(f"Operadora: {__carrier}")
print(f"Estado: {__region}")
