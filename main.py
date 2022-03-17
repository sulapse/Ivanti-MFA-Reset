from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import customers
#import os

#UNLOCK ACCOUNT BEKRÄFTAR ALDRIG UPPLÅSNINGEN, fixa.

#inlogg och alternativ för webdriver
myuser = "kesu"
mypass = "a0bTxT123Myh41k2o"
options = Options()
#options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#os.environ['WDM_LOG_LEVEL'] = '0'

###Väljer driver och öppnar webbläsare med url från customers.py
#browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe', options=options)
#browser.get(customers.foretagurl)
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get(customers.foretagurl)


#PostLogin hanterar allt från "startsidan" efter lyckad inloggning. I.e välja auth server, och navigera till listan över users.
#PostLogin innehåller också hantering av autocomplete för användarnamnen
def PostLogin():

    authservers = browser.find_element(By.XPATH,
                                       '/html/body/table[5]/tbody/tr[1]/td[1]/table/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/a')
    authservers.click()

    totpselect = browser.find_element(By.LINK_TEXT, customers.foretagotp)
    totpselect.click()
    userselect = browser.find_element(By.XPATH,
                                      '/html/body/table[5]/tbody/tr[2]/td[3]/form/table[3]/tbody/tr[1]/td/table/tbody/tr[1]/td[3]/table/tbody/tr/td/a')
    userselect.click()

    rubrik = browser.find_element(By.CLASS_NAME, 'cssPgTitle').text
    print(rubrik)

    showxusers = browser.find_element(By.XPATH, '//*[@id="matchCount_6"]')
    showxusers.clear()
    showxusers.send_keys('69420' + Keys.ENTER)

    userslist = []
    table_tbody = browser.find_element(By.XPATH, '/html/body/table[5]/tbody/tr/td[5]/table[6]/tbody')
    rows = table_tbody.find_elements(By.XPATH, "//*[starts-with(@id, 'trItem')]")
    for row in rows:
        col = row.find_element(By.XPATH, 'td[2]')
        userslist.append(col.text)

    #print(userslist)
    userlistcompleter = WordCompleter(userslist)
    customer = prompt('Användarnamn?: ', completer=userlistcompleter)


    customersel = browser.find_element(By.ID, customer + ":" + rubrik)
    customersel.click()

    unlockresetcomplete = WordCompleter(['unlock', 'reset'])
    unlockresetinput = prompt('unlock / reset? ', completer=unlockresetcomplete)



    if unlockresetinput == "unlock":
        unlockuser = browser.find_element(By.XPATH, '//*[@id="btnUnlock_49"]')
        unlockuser.click()
        print("Success! Account has been unlocked.")
    elif unlockresetinput == "reset":
        resetuser = browser.find_element(By.XPATH, '//*[@id="btnReset_49"]')
        resetuser.click()
        resetconfirm = browser.find_element(By.XPATH, '//*[@id="btnConfirmReset"]')
        resetconfirm.click()
        print("Success! Account has been reset.")


#Om aktiv session redan finns klickar på continue
def continueses():
    btncheck = browser.find_element(By.NAME, 'btnContinue')
    btncheck.click()
    checknewUI()


#Byter till klassiska UI om det inte redan finns en aktiv session
def changefromnewUI():
    newnavbar = browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/a')
    newnavbar.click()
    switchnewUI = browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/ul/li[3]/a')
    switchnewUI.click()
    PostLogin()


#Gör en check om nuvarande UI är nya eller klassiska
def checknewUI():
    try:
        browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/a')
    except NoSuchElementException:
        print("Not new UI")
        PostLogin()
    else:
        print("New UI")
        changefromnewUI()


#Skriver in user och pass samt loggar in på loginsidan
loginuser = browser.find_element(By.XPATH, '//*[@id="username"]')
loginpass = browser.find_element(By.XPATH, '//*[@id="password"]')
loginuser.send_keys(myuser)
loginpass.send_keys(mypass + Keys.ENTER)

#Gör check om det redan finns en aktiv session
try:
    browser.find_element(By.NAME, 'btnContinue')
except NoSuchElementException:
    print("except")
    PostLogin()
else:
    print("else")
    continueses()
