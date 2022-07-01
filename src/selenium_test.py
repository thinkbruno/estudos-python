# PEP8 OK
# -*- coding: utf-8 -*-

# pip install selenium
# pip install chromedriver-autoinstaller
import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.python.org/")
time.sleep(5)
driver.quit()
