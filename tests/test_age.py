import pytest
from app.services.age import calculate_age_detailed

def test_valid_age():
    result = calculate_age_detailed("2000-01-01")
    assert result["years"] >= 0

def test_less_than_one_year():
    from datetime import date
    today = date.today()
    birth = today.replace(month=today.month - 1 if today.month > 1 else 1)
    result = calculate_age_detailed(birth.strftime("%Y-%m-%d"))
    assert result["years"] == 0

def test_invalid_format():
    with pytest.raises(ValueError):
        calculate_age_detailed("01-01-2000")

def test_future_date():
    with pytest.raises(ValueError):
        calculate_age_detailed("3000-01-01")
