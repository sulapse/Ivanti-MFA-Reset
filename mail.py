import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

testin = input("USERNAME: ")


def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our HTML email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "wchqxfkyotwyxesy"

    server.starttls()
    server.login(FROM, password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()


if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
    email_content = """
<!DOCTYPE html
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:v="urn:schemas-microsoft-com:vml" lang="en">

<head>
  <link rel="stylesheet" type="text/css" hs-webfonts="true"
    href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
  <title>Email template</title>
  <meta property="og:title" content="Email template">

  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style type="text/css">
    a {
      text-decoration: underline;
      color: inherit;
      font-weight: bold;
      color: #253342;
    }

    h1 {
      font-size: 42px;
      font-weight: 100;
      margin: 40px;
      margin-bottom: 60px;
    }

    h2 {
      font-size: 28px;
      font-weight: 900;
    }

    p {
      font-weight: 100;
    }

    td {
      vertical-align: top;
    }

    button {
      font: inherit;
      background-color: #FBE122;
      border: none;
      margin-top: 16px;
      padding: 12px 24px;
      text-transform: uppercase;
      letter-spacing: 2px;
      font-weight: 900;
      color: black;
      border-radius: 5px;
      box-shadow: 3px 3px #fb9d22b0;
    }

    .Logo {
      padding-top: 150px;
    }

    .subtle-link {
      font-size: 9px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #494949;
    }

    .container {
      margin: auto;
      width: 800px;
      background-color: white;
    }

    .firstRow {
      width: auto;
    }

    .secondRow {
      width: auto;
    }

    .column {
      width: 320px;
    }
  </style>

</head>

<body style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#1D3C34; word-break:break-word; background-color: #F2F2F2">

  <! View in Browser Link -->

    <div class="container">
      <table align="right" role="presentation">
        <tr>
          <td>
            <a class="subtle-link" href="#">href</a>
          </td>
        <tr>
      </table>

      <! Banner -->
        <table class="Banner" role="presentation" width="100%">
          <tr>

            <td bgcolor="#1D3C34" align="center" style="color: white;">

              <img class="Logo" alt="Flower" src="https://i.imgur.com/tfygkC6.png"
                width="400px" align="middle">

              <h1> """ + str(testin) + """ </h1>

            </td>
        </table>

        <! First Row -->

          <table class="firstRow" role="presentation" border="0" cellpadding="10" cellspacing="0px"
            style="padding: 30px 60px 30px 60px;">
            <tr>
              <td>
                <h2>Kevin trodde han var cool...</h2>
                <p>
                  För han hade en pistol. Grabbens pistol var en pluggad kopia
                  när ja tog upp min Uzi utbrast han; Mamma mia!
                  Han hade tur att ja hade humor
                  och inte ville slösa mina kulor.
                </p>
                <button>
                  Hämta mer ammo
                </button>
              </td>
            </tr>
          </table>

          <! Second Row with Two Columns-->

            <table class="secondRow" role="presentation" cellpadding="10" cellspacing="0px" width="100%"
              style="padding: 30px 60px 30px 60px;">
              <tr>
                <td class="column">

                    <img alt="Blog"
                      src="https://www.hubspot.com/hubfs/assets/hubspot.com/style-guide/brand-guidelines/guidelines_sample-illustration-3.svg"
                      width="200px" align="middle">

                    <h2> Vivamus ac elit eget </h2>
                    <p>
                      Vivamus ac elit eget dolor placerat tristique et vulputate nibh. Sed in elementum nisl, quis
                      mollis
                      enim. Etiam gravida dui vel est euismod, at aliquam ipsum euismod.
                    </p>

                </td>

                <td class="column">

                  <img alt="Shopping"
                    src="https://www.hubspot.com/hubfs/assets/hubspot.com/style-guide/brand-guidelines/guidelines_sample-illustration-5.svg"
                    width="200px" align="center">
                  <h2> Suspendisse tincidunt iaculis </h2>
                  <p>
                    Suspendisse tincidunt iaculis fringilla. Orci varius natoque penatibus et magnis dis parturient
                    montes, nascetur ridiculus mus. Cras laoreet elit purus, quis pulvinar ipsum pulvinar et.

                  </p>
                </td>
              </tr>

              <tr>
                <td> <button> Button 2 </button> </td>
                <td> <button> Button 3 </button> </td>

            </table>

            <! Kontakta oss -->
              <table role="presentation" bgcolor="#F3DCC6" width="100%" style="margin-top: 50px;">
                <tr>
                  <td align="center" style="padding: 30px 30px;">

                    <h2> Kontakta oss </h2>
                    <p>
                      Servicedesk: 08-6929270<br>Växel: 08-6929200
                    </p>
                    <p>Norra Stationsgatan 61<br>113 13, Stockholm</p>
                    <a href="#">Fråga oss</a>
                  </td>
                </tr>
              </table>

              <! Skapat med kärlek -->

                <table role="presentation" bgcolor="#F2F2F2" width="100%">
                  <tr>
                    <td align="left" style="padding: 30px 0px;">
                      <p style="color:#99ACC2">Made with &hearts; at Nordlo Stockholm City AB </p>

                    </td>
                  </tr>
                </table>
    </div>
</body>

</html>
"""

    TO = 'kevinzundin@gmail.com'
    FROM = 'kevinzundin@gmail.com'

    py_mail("Test email subject", email_content, TO, FROM)
