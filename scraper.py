from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
webdriver = webdriver.Chrome(
chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)


webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('spectrammedia')
password = webdriver.find_element_by_name('password')
password.send_keys('Backsp@c5')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
button_login.click()
sleep(3)

#notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
#notnow.click() #comment