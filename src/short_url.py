# PEP8 OK
# -*- coding: utf-8 -*-

import os
import pyshorteners

from dotenv import load_dotenv
load_dotenv()

"""encurtando urls
"""

url = os.getenv("URL")

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(url)

print(f"URL encurtada: {short_url}")
