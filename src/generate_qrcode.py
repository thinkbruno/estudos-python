# PEP8 OK
# -*- coding: utf-8 -*-

import os
import pyqrcode

from dotenv import load_dotenv
load_dotenv()

"""criando qrcode a partir de uma URL (adicionar um arquivo .env)
"""

url = os.getenv("URL")

qr_code = pyqrcode.create(url)

qr_code.png(r'new_qrcode.png', scale=8)
