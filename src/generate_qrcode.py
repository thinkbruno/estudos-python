# PEP8 OK
# -*- coding: utf-8 -*-

import pyqrcode

url = 'https://allmylinks.com/ramosbruno90'

qr_code = pyqrcode.create(url)

qr_code.png(r'new_qrcode.png', scale=8)
