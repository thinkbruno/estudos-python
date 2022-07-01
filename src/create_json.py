# PEP8 OK
# -*- coding: utf-8 -*-

import json

from faker import Faker

obj_fake = Faker()

obj = {
    "Nome": obj_fake.name(),
    "Usuario": obj_fake.user_name(),
    "Senha": obj_fake.password(),
    "Dados Pessoais": {
        "Nome da mãe": obj_fake.first_name_female(),
        "Mês de Nascimento": obj_fake.month()
    }
}

try:
    with open(r'.\src\data.json', 'w', encoding='utf8') as json_file:
        json.dump(obj, json_file, indent=4, ensure_ascii=False)
    print('Arquivo concluído')
except:
    raise FileNotFoundError
