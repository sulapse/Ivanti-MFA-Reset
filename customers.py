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

#print("URL: ",admUrl[0])
#print("TOTP: ", custTotp[0])


mydb.close()

# Lista över företag, deras URL och länknamn för TOTP på pulse admin sidan.
#if foretaginput == "sigtunahem":
#    foretagurl = "https://ssl-sigtunahem.dcloud.se/admin"
#    foretagotp = "Sigtunahem-totp"
#elif foretaginput == "besqab":
#    foretagurl = "https://ssl-besqab.dcloud.se/admin"
#    foretagotp = "Besqab_TOTP"
#elif foretaginput == "structor":
#    foretagurl = "https://ssl-structor.dcloud.se/admin"
#    foretagotp = "Structor_TOTP"
#elif foretaginput == "akademikerförbundet":
#    foretagurl = "https://ssl-akademssr.dcloud.se/admin"
#    foretagotp = "Akademssr_TOTP"
#elif foretaginput == "swedish_stirling":
#    foretagurl = "https://ssl-swedishstirling.dcloud.se/admin"
#    foretagotp = "Stirling-TOTP"
#elif foretaginput == "nordia":
#    foretagurl = "https://ssl-nordia.dcloud.se/admin"
#    foretagotp = "Nordia_TOTP"
#elif foretaginput == "bengtdahlgren_gbg":
#    foretagurl = "https://ssl-bd.dcloud.se/admin"
#    foretagotp = "BDABGBG-TOTP"
#elif foretaginput == "bengtdahlgren_br":
#    foretagurl = "https://ssl-bor.dcloud.se/admin"
#    foretagotp = "BOR-TOTP"
#elif foretaginput == "aaro":
#    foretagurl = "https://access.aarocloud.com/admin"
#    foretagotp = "Aarocloud_TOTP"
#elif foretaginput == "kinnevik":
#    foretagurl = "https://ssl-k.dcloud.se/admin"
#    foretagotp = "Kinnevik-TOTP"
#elif foretaginput == "sarnmark":
#    foretagurl = "https://ssl-sarnmark.dcloud.se/admin"
#    foretagotp = "Sarnmark TOTP"
#elif foretaginput == "energiforetagen":
#    foretagurl = "https://ssl-energiforetagen.dcloud.se/admin"
#    foretagotp = "Energiforetagen_TOTP"
#elif foretaginput == "kungalvsbostader":
#    foretagurl = "https://ssl-kungalvsbostader.dcloud.se/admin"
#    foretagotp = "Kungalv_TOTP"
#elif foretaginput == "srat":
#    foretagurl = "https://ssl-sverigesingenjorer.dcloud.se/admin"
#    foretagotp = "SRAT-TOTP"
#elif foretaginput == "nordlo_stockholm_city":
#    foretagurl = "https://ssl.dicom.se/admin"
#    foretagotp = "Dicom_TOTP"
#elif foretaginput == "norstedts":
#    foretagurl = "https://ssl-norstedts.dcloud.se/admin"
#    foretagotp = "Norstedts_TOTP"
#elif foretaginput == "skandia":
#    foretagurl = "https://ssl-skandiafastigheter.dcloud.se/admin"
#    foretagotp = "Skandia-TOTP"