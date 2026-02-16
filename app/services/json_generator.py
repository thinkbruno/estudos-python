import json
from faker import Faker
from io import BytesIO


def generate_json_file():
    fake = Faker()

    data = {
        "nome": fake.name(),
        "usuario": fake.user_name(),
        "senha": fake.password(),
        "dados_pessoais": {
            "nome_mae": fake.first_name_female(),
            "mes_nascimento": fake.month(),
        },
    }

    json_bytes = json.dumps(data, indent=4, ensure_ascii=False).encode("utf-8")

    return BytesIO(json_bytes)
