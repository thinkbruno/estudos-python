# PEP8 OK
# -*- coding: utf-8 -*-

import random
import string

"""Gerador de senhas de até 16 caracteres
"""

def generate_password(length):
    allowed_chars = '!&*$@#?'

    upper_case = random.choice(string.ascii_uppercase)
    lower_case = random.choice(string.ascii_lowercase)
    special = random.choice(allowed_chars)
    numbers_and_specials = ''.join(random.choice(string.digits + allowed_chars) for _ in range(length - 3))

    password = upper_case + lower_case + special + numbers_and_specials
    password = ''.join(random.sample(password, length))  # Embaralha os caracteres válidos

    return password

password = generate_password(16)
print(password)