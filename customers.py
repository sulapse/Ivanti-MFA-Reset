from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


print("<<<MFA Reset V0.1>>>")
#masterkey = input("Master key?: ")
# if masterkey != "SuperSecret":
#    quit()

cust_completer = WordCompleter(
    ['besqab', 'sigtunahem', 'structor', 'akademikerförbundet', 'swedish_stirling', 'nordia', 'bengtdahlgren_gbg', 'bengtdahlgren_br', 'aaro', 'kinnevik', 'sarnmark', 'energiforetagen', 'kungalvsbostader'])
foretaginput = prompt('Företag: ', completer=cust_completer)

# Lista över företag, deras URL och länknamn för TOTP på pulse admin sidan.
if foretaginput == "sigtunahem":
    foretagurl = "https://ssl-sigtunahem.dcloud.se/admin"
    foretagotp = "Sigtunahem-totp"
elif foretaginput == "besqab":
    foretagurl = "https://ssl-besqab.dcloud.se/admin"
    foretagotp = "Besqab_TOTP"
elif foretaginput == "structor":
    foretagurl = "https://ssl-structor.dcloud.se/admin"
    foretagotp = "Structor_TOTP"
elif foretaginput == "akademikerförbundet":
    foretagurl = "https://ssl-akademssr.dcloud.se/admin"
    foretagotp = "Akademssr_TOTP"
elif foretaginput == "swedish_stirling":
    foretagurl = "https://ssl-swedishstirling.dcloud.se/admin"
    foretagotp = "Stirling-TOTP"
elif foretaginput == "nordia":
    foretagurl = "https://ssl-nordia.dcloud.se/admin"
    foretagotp = "Nordia_TOTP"
elif foretaginput == "bengtdahlgren_gbg":
    foretagurl = "https://ssl-bd.dcloud.se/admin"
    foretagotp = "BDABGBG-TOTP"
elif foretaginput == "bengtdahlgren_br":
    foretagurl = "https://ssl-bor.dcloud.se/admin"
    foretagotp = "BOR-TOTP"
elif foretaginput == "aaro":
    foretagurl = "https://access.aarocloud.com/admin"
    foretagotp = "Aarocloud_TOTP"
elif foretaginput == "kinnevik":
    foretagurl = "https://ssl-k.dcloud.se/admin"
    foretagotp = "Kinnevik-TOTP"
elif foretaginput == "sarnmark":
    foretagurl = "https://ssl-sarnmark.dcloud.se/admin"
    foretagotp = "Sarnmark TOTP"
elif foretaginput == "energiforetagen":
    foretagurl = "https://ssl-energiforetagen.dcloud.se/admin"
    foretagotp = "Energiforetagen_TOTP"
elif foretaginput == "kungalvsbostader":
    foretagurl = "https://ssl-kungalvsbostader.dcloud.se/admin"
    foretagotp = "Kungalv_TOTP"
else:
    print("Kunden finns ej, försök igen!")
    input("Klicka ENTER för att börja om..")
    quit()
