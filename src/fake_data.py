# PEP8 OK
# -*- coding: utf-8 -*-

# pip install faker
from faker import Faker

obj_fake = Faker()

name = obj_fake.name()
first_name_female = obj_fake.first_name_female()
user_name = obj_fake.user_name()
password = obj_fake.password()
month = obj_fake.month()


print(f"Nome: {name}")
print(f"Nome feminino: {first_name_female}")
print(f"Usuário: {user_name}")
print(f"Senha: {password}")
print(f"Mês: {month}")
