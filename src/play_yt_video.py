# PEP8 OK
# -*- coding: utf-8 -*-

import os
import pywhatkit as kit

from dotenv import load_dotenv
load_dotenv()

"""executando video do youtube, adicionar link no seu .env
"""

url = os.getenv("YT_VIDEO_URL")

kit.playonyt(url)
