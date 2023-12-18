# PEP8 OK
# -*- coding: utf-8 -*-

import psutil
import sys

"""verificando porcentagem da pateria, usando lib psutil
"""
battery = psutil.sensors_battery()
if battery:
    percent = int(battery.percent)
    print(f'{percent}%')
else:
    print('Você precisa de uma bateria para ter o status da bateria.')
    sys.exit
