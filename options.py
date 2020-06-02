import pytesseract
from selenium import webdriver

pytesseract.pytesseract.tesseract_cmd = 'tesseract' # cmd command for tesseract or path to executable file (windows)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.binary_location = '/usr/bin/chromium-browser' # Chrome browser location
options.add_argument('--headless') # Comment to show browser window

path_driver = './chromedriver_mac'  # full path to chromedriver_mac

# Mail client settings

from_mail = 'noreply@your.mail'
from_passwd = 'yourcoolpassword'
smtp_server = 'smtp.yandex.ru'
smtp_port = '465'



