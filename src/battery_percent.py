# PEP8 OK
# -*- coding: utf-8 -*-

import psutil

battery = psutil.sensors_battery()

percent = int(battery.percent)

print(f'{percent}%')
