from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import mysql.connector
from main import clearall


mydb = mysql.connector.connect(
    host="10.1.3.10",
    user="kevin",
    passwd="cody123",
    database="mfa_reset"
)

customerList = []

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
customers = mycursor.fetchall()

for row in customers:
    customerList.append(row[1])


cust_completer = WordCompleter(customerList)
custInput = prompt('Företag: ', completer=cust_completer)

while custInput not in customerList:
    clearall()
    print("Kunden finns ej, Försök igen.")
    custInput = prompt('Företag: ', completer=cust_completer)


mycursor.execute(f"SELECT pulseadminurl_cust, pulsetotopurl_cust FROM customers WHERE custname_cust='{custInput}'")
custdata = mycursor.fetchall()


admUrl = [item[0] for item in custdata]
custTotp = [item[1] for item in custdata]
userUrl = admUrl[0].replace('/admin', '')



mydb.close()
