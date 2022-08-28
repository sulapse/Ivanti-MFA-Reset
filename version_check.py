from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_argument('--headless')
os.environ['WDM_LOG_LEVEL'] = '0'
service = ChromeService(executable_path=ChromeDriverManager().install())

vercheck = webdriver.Chrome(service=service, options=options)
vercheck.get("https://raw.githubusercontent.com/sulapse/test/main/version")
version = vercheck.find_element(By.XPATH, '/html/body/pre')

print(version.text)

if version.text == "1.1":
    print("Du är på senaste versionen!")
else:
    print("Vill du ladda ner senaste versionen?")
    uppdatera = input("Y / N: ")
    if uppdatera == "Y":
        vercheck.get("https://google.com")
    elif uppdatera == "N":
        print("Well too bad, bye.")
