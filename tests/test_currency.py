import pytest
from unittest.mock import patch
from app.services.currency import convert_usd_to_brl


def test_conversion_success():
    with patch("app.services.currency.CurrencyRates.convert") as mock_convert:
        mock_convert.return_value = 5.25
        result = convert_usd_to_brl(10)
        assert result == 5.25


def test_invalid_amount():
    with pytest.raises(ValueError):
        convert_usd_to_brl(0)
