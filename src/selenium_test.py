# PEP8 OK
# -*- coding: utf-8 -*-

import time

import chromedriver_autoinstaller
from selenium import webdriver

"""testando uso de selenium
"""

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.python.org/")
time.sleep(5)
driver.quit()
