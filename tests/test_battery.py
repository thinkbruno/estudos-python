import pytest
from unittest.mock import patch
from app.services.battery import get_battery_percent, BatteryNotFoundError


def test_battery_success():
    with patch("app.services.battery.psutil.sensors_battery") as mock_battery:
        mock_battery.return_value = type("Battery", (), {"percent": 80})()
        assert get_battery_percent() == 80


def test_battery_not_found():
    with patch("app.services.battery.psutil.sensors_battery") as mock_battery:
        mock_battery.return_value = None
        with pytest.raises(BatteryNotFoundError):
            get_battery_percent()
