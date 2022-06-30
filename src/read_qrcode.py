# PEP8 OK
# -*- coding: utf-8 -*-

# pip install pillow
# pip install pyzbar
import webbrowser

from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('qrcode.png'))

webbrowser.open(read[0].data)
