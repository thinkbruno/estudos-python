# PEP8 OK
# -*- coding: utf-8 -*-

import random

"""Gerador de senhas de até 8 caracteres
"""

upper_case = chr(random.randint(65, 90))
lower_case = chr(random.randint(97, 122))
special = chr(random.randint(33, 38))
list_numbers = ''.join(str(random.randrange(9)) for _ in range(5))

print(f"{upper_case}{lower_case}{list_numbers}{special}")