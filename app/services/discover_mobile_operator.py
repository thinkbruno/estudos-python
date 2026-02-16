import phonenumbers
from phonenumbers import carrier, geocoder


def get_mobile_operator_info(number: str) -> dict:
    try:
        phone_number = phonenumbers.parse(f"+55{number}")

        operator = carrier.name_for_number(phone_number, "pt-br")
        region = geocoder.description_for_number(phone_number, "pt-br")

        return {
            "operadora": operator or "Não identificada",
            "estado": region or "Não identificado",
        }

    except Exception:
        raise ValueError("Número inválido")
