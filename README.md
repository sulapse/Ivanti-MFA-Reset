# Ivanti Secure MFA Reset
<br>
Hello there!<br>
Since the developers of Pulse / Ivanti Secure are crackheads and decided to make the admin panels unique for each customer I wrote this script to bring them together in to one place and automate the reset of MFA and account unlocks using Python and the Selenium framework.<br>
<br>
It features "auto-updating" using the Github API and checking the "version" file for the current version, not a bad solution, not a good one either.
<br>

## Requirements
* Python 3.x
* Python packages in requirements.txt
* MySQL DB
* Google Chrome browser

## Getting started
1. Clone the repository
2. Configure the MySQL DB
* You need 1 DB, 1 Table and 4 Columns.
* Table name: customers
* Columns:
  * id_cust (Unique ID from 0 to x)
  * custname_cust (Name of each customer, (is used to autcomplete when searching for a customer in the script))
  * pulseadminurl_cust (The Ivanti Secure admin url for that customer ("https://ssl-customer.com/admin"))
  * pulsetotopurl_cust (Ivanti secure totp URL for that customer (https://ssl-customer.com/dana-admin/user/findTOTP.cgi?selauthserver=1&authname=5&authtype=TOTP))
3. In main.py:
* Replace line 31 with your Github API token
* Replace line 33 with another URL to check for the current version
* Replace line 39 with the download URL to the newest version of mfa reset
* Replace line 60 - 63 with your own DB config
* Replace line 94 with an Ivanti Secure admin URL (Used for checking the credentials)
* Replace both instances of "PULSEURL" on line 102 with the same url you added on line 94
4. In customers.py
* Replace line 8 - 11 with the same DB config as from Main.py

That should be everything, now run python main.py
