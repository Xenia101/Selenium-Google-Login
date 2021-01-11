# -*- coding: utf-8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

GOOGLE_LOGIN_PATH = os.getenv('GOOGLE_LOGIN_PATH')  # Google login bypass URL
# user_data_dir     = os.getenv('USER_DATA_DIR')    # USER-DATA-DIR

GOOGLE_ID = os.getenv('GOOGLE_ID') # google id
GOOGLE_PW = os.getenv('GOOGLE_PW') # google pwd

options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=" + user_data_dir)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options) 

# Selenium Google Login bypass URL
driver.get(GOOGLE_LOGIN_PATH)

# email login 
login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
login.send_keys(GOOGLE_ID)

# click next
driver.find_element_by_id('identifierNext').click()

# password
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password = password.find_element_by_tag_name('input')
password.send_keys(GOOGLE_PW)

# click next
driver.find_element_by_id('passwordNext').click()

# wait
# time.sleep(100)

# close window
driver.close()