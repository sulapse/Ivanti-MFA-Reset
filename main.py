from turtle import clear
from stdiomask import getpass
from importlib import reload
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import logging
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


#Funktion för att tömma konsollen och printa programmets titel
def clearall():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    print("<<< MFA Reset V1.0 >>>")

#Vid start av skriptet stängs loggar av och definierar samt kör browser med options
if __name__ == '__main__':
    os.environ['WDM_LOG'] = str(logging.NOTSET)
    os.environ['WDM_LOG_LEVEL'] = '0'
    ###alternativ för webdriver
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.add_argument('--headless')
    service = ChromeService(executable_path=ChromeDriverManager().install())

###PulsePWCheck gör ett inloggningsförsök i Pulse för Structor
###Om inlogg lyckas hoppar skriptet vidare till VeryBeginning()
    def PulsePWCheck():
        clearall()
        testlogin = webdriver.Chrome(service=service, options=options)
        testlogin.get("https://ssl-structor.dcloud.se/admin")
        print("[Skriv in dina admin uppgifter för Pulse Secure]")
        while True:
            clearall()
            myuser = input("Användarnamn: ")
            if myuser != '':
                break
        while True:
            clearall()
            mypass = getpass("Lösenord: ")
            if mypass != '':
                break

        testlogin.find_element(By.XPATH, '//*[@id="username"]').send_keys(myuser)
        testlogin.find_element(By.XPATH, '//*[@id="password"]').send_keys(mypass + Keys.ENTER)
        try:
            testlogin.find_element(By.XPATH, '//*[@id="table_LoginPage_5"]/tbody/tr[1]/td')
        except NoSuchElementException:
            if testlogin.current_url == "https://ssl-structor.dcloud.se/dana-admin/misc/dashboard.cgi" or testlogin.current_url == "https://ssl-structor.dcloud.se/dana-na/auth/url_admin/welcome.cgi?p=admin%2Dconfirm":
                clearall()
                print("[Inlogg OK]")
                testlogin.close()
                VeryBeginning(myuser, mypass)
            else:
                clearall()
                print("Fel användarnamn eller lösenord, försök igen.")
                testlogin.close()
                PulsePWCheck()
        else:
            clearall()
            print("Fel användarnamn eller lösenord, försök igen.")
            testlogin.close()
            PulsePWCheck()


##VeryBeginning startar bara ny browser och tillåter skriptet att loopa
##Ansluter till MySQL för att hämta användarna och företagens URLer mm mha customers.py
##Efter navigering till URL, kör checknewui, changefromnewUI, continueses
    def VeryBeginning(myuser, mypass):
        import customers
        clearall()
        print("Letar efter sågspån..")
        ###Väljer driver och öppnar webbläsare med url från customers.py
        browser = webdriver.Chrome(service=service, options=options)
        browser.get(customers.admUrl[0])

        ###PostLogin hanterar allt från "startsidan" efter lyckad inloggning. I.e välja auth server, och navigera till listan över users.
        ###PostLogin innehåller också hantering av autocomplete för användarnamnen
        def PostLogin():
            browser.get(customers.custTotp[0])
            clearall()
            print("Laddar användarna..")
            showxusers = browser.find_element(By.XPATH, '//*[@id="matchCount_6"]')
            showxusers.clear()
            showxusers.send_keys('69420' + Keys.ENTER)

            userslist = []
            table_tbody = browser.find_element(By.XPATH, '/html/body/table[5]/tbody/tr/td[5]/table[6]/tbody')
            rows = table_tbody.find_elements(By.XPATH, "//*[starts-with(@id, 'trItem')]")
            for row in rows:
                col = row.find_element(By.XPATH, 'td[2]')
                userslist.append(col.text)

            # print(userslist)
            clearall()
            print("Pulse Secure användarinlogg: " + customers.userUrl)
            print("[Lämna användarnamn blankt och klicka ENTER för att återgå till välja företag]")
            userlistcompleter = WordCompleter(userslist)
            customer = prompt('Användarnamn?: ', completer=userlistcompleter)

            if customer == '':
                clearall()
                browser.close()
                reload(customers)
                VeryBeginning(myuser, mypass)
            else:
                while customer not in userslist:
                    clearall()
                    print("Pulse Secure användarinlogg: " + customers.userUrl)
                    print("Användaren kan ej hittas, försök igen.")
                    customer = prompt('Användarnamn?: ', completer=userlistcompleter)
                    if customer == '':
                        clearall()
                        browser.close()
                        reload(customers)
                        VeryBeginning(myuser, mypass)

            #Klickar på användarens checkbox i Pulse
            browser.find_element(By.XPATH, "//input[contains(@id,'{}')]".format(str(customer))).click()

            #Ger användaren valet att låsa upp eller återställa kontot som blivit valt
            print("Pulse Secure användarinlogg: " + customers.userUrl)
            unlockresetcomplete = WordCompleter(['unlock', 'reset'])

            #Loopar till användaren valt lås upp eller lås upp
            while True:
                clearall()
                print("Pulse Secure användarinlogg: " + customers.userUrl)
                print("Vald användare:", customer)
                unlockresetinput = prompt('unlock / reset: ', completer=unlockresetcomplete)
                if unlockresetinput == "unlock":
                    browser.find_element(By.XPATH, '//*[@id="btnUnlock_49"]').click()
                    try:
                        unlockconfirm = browser.find_element(By.XPATH, '//*[@id="btnConfirmUnlock"]')
                    except NoSuchElementException:
                        clearall()
                        print("Kontot är redan upplåst!")
                        print("[Återgår till val av företag om 5 sekunder..]\n")
                        print("Pulse Secure användarinlogg: " + customers.userUrl)
                        time.sleep(5)
                        clearall()
                        break
                    else:
                        unlockconfirm.click()
                        clearall()
                        print("Kontot har blivit upplåst!")
                        print("[Återgår till val av företag om 5 sekunder..]\n")
                        print("Pulse Secure användarinlogg: " + customers.userUrl)
                        time.sleep(5)
                        clearall()
                        break

                ##Om user kör valet "reset", klickar på reset och printar godkännelse
                elif unlockresetinput == "reset":
                    resetuser = browser.find_element(By.XPATH, '//*[@id="btnReset_49"]').click()
                    resetconfirm = browser.find_element(By.XPATH, '//*[@id="btnConfirmReset"]').click()
                    clearall()
                    print("Lyckat! Konto har blivit återställt.")
                    print("[Återgår till val av företag om 5 sekunder..]\n")
                    print("Pulse Secure användarinlogg: " + customers.userUrl)
                    time.sleep(5)
                    clearall()
                    break

            browser.close()
            reload(customers)
            VeryBeginning(myuser, mypass)

        ##Om aktiv session redan finns klickar på continue
        def continueses():
            browser.find_element(By.NAME, 'btnContinue').click()
            checknewUI()

        ##Byter till klassiska UI om det inte redan finns en aktiv session
        def changefromnewUI():
            browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/a').click()
            browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/ul/li[3]/a').click()
            PostLogin()

        ##Gör en check om nuvarande UI är nya eller klassiska
        def checknewUI():
            try:
                browser.find_element(By.XPATH, '//*[@id="navbartop_right"]/a')
            except NoSuchElementException:
                PostLogin()
            else:
                changefromnewUI()


        ##Skriver in user och pass samt loggar in på loginsidan
        browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(myuser)
        browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(mypass + Keys.ENTER)

        ##Gör check om det redan finns en aktiv session
        try:
            browser.find_element(By.NAME, 'btnContinue')
        except NoSuchElementException:
            PostLogin()
        else:
            continueses()


    PulsePWCheck()
    