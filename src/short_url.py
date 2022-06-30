# PEP8 OK
# -*- coding: utf-8 -*-

import pyshorteners

# pip install pyshorteners


url = 'https://allmylinks.com/ramosbruno90'

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(url)

print(f"URL encurtada: {short_url}")
