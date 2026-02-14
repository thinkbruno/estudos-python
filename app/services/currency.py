from forex_python.converter import CurrencyRates
from forex_python.converter import RatesNotAvailableError


class CurrencyConversionError(Exception):
    pass


def convert_usd_to_brl(amount: float) -> float:
    """
    Converte USD para BRL usando cotação atual.
    """

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    c = CurrencyRates()

    try:
        result = c.convert("USD", "BRL", amount)
    except RatesNotAvailableError:
        raise CurrencyConversionError("Exchange rate not available.")
    except Exception:
        raise CurrencyConversionError("Error fetching exchange rate.")

    return round(result, 2)
