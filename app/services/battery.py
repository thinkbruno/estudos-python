import psutil


class BatteryNotFoundError(Exception):
    pass


def get_battery_percent() -> int:
    """
    Retorna a porcentagem atual da bateria.
    """
    battery = psutil.sensors_battery()

    if battery is None:
        raise BatteryNotFoundError("No battery detected on this system.")

    return int(battery.percent)
