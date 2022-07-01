# PEP8 OK
# -*- coding: utf-8 -*-

import webbrowser

from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('qrcode.png'))

webbrowser.open(read[0].data)
