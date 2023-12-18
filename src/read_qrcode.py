# PEP8 OK
# -*- coding: utf-8 -*-

import webbrowser

from PIL import Image
from pyzbar.pyzbar import decode

"""lendo qr code
"""

read = decode(Image.open('new_qrcode.png'))

webbrowser.open(read[0].data)
