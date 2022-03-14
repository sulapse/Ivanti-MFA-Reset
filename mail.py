import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><meta name="viewport" content="width=device-width, initial-scale=1">

        <!--[if mso]>
        <xml>
           <o:OfficeDocumentSettings>
              <o:AllowPNG/>
              <o:PixelsPerInch>96</o:PixelsPerInch>
           </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <!-- [if mso]>
         <style>
            body, table tr, table td, a, span, table.MsoNormalTable {
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif !important;
            }
        </style>
        <!--<![endif]-->
</head>
<body style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; margin: 0; padding: 0;">
    <table align="center" valign="center" role="presentation" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;width:100%;background-color:#f2f2f2">
        <tbody>
            <tr>
                    <td align="center" valign="center" style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; font-style: normal; font-weight: normal;">
                        <table role="presentation" dir="ltr" border="0" width="600" cellpadding="0" cellspacing="0" align="center" style="table-layout: fixed; border-collapse: collapse; border-spacing: 0; max-width: 600px;" bgcolor="#FAF9F8">
                            <tbody>



    <tr bgcolor="#1D3C34">
        <td style="height: 70px; padding: 0 20px">
            <table role="presentation" border="0" style="width: 560px; color: #F3DBC6">
                <tbody>
                    <tr>
                        <td height="32" style="font-size: 24px;">
                                <img src="cid:ac809f57-54ec-4d29-bff4-fac494fc1d61" alt="Your company logo" height="32" style="vertical-align: middle;">
                        </td>
                        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; text-align: right; font-size: 12px; line-height: 16px;">
                            Sunday, 16 Jan, 2022
                        </td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
    <tr>
        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; padding: 16px 16px 12px 16px; font-size: 20px; line-height: 106.2%; letter-spacing: -0.5px; color: #000000; font-weight: 500;">
            Hello <b>Kevin Sundin</b>
        </td>
    </tr>
    <tr>
        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; padding-left: 16px; padding-right: 16px; font-size: 14px; line-height: 16px; color: #000000;">
            Here's some news you might have missed this past week.
        </td>
    </tr>
    <tr>
        <td style="padding: 12px 16px 16px 16px;">
            <table role="presentation" cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td bgcolor="#ffffff" style=" padding: 6px 17px; border: 1px solid #000000;border-radius: 0px;font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; font-size: 12px; text-decoration: none; display: inline-block;">
                        <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnordlo.sharepoint.com%2F_layouts%2F15%2Fsharepoint.aspx%3Fv%3Dnews%26e%3DYr88zdZ_FUiJ6V7VEmfMBA%26at%3D38&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=gu%2F5WpiLq4135qWM31dDrTKL1JtWZCIKpsFOKhrDcgU%3D&amp;reserved=0" originalsrc="https://nordlo.sharepoint.com/_layouts/15/sharepoint.aspx?v=news&amp;e=Yr88zdZ_FUiJ6V7VEmfMBA&amp;at=38" shash="cU8gD4WhGksghkHl1O0EPxbbk8i3lkJ65C/fKcDI2k6/A2wKaaAzH6BlI1+EX5VOvO3ZCQ2Kn90QSDgwHG6B+QjW5QFEycdwMHbBJgASoqXGhquS2fLMuofDl3cFdDMPJHxWaU2teqI/j90Pn6FlSGNI8tPwWbpIAPPad8Sir+I=" style="color: #000; text-decoration: none; " target="_blank">
                            See all news
                        </a>
                    </td>
                </tr>
            </tbody></table>

        </td>

    </tr>



        <tr>
            <td width="568" height="200" style="padding: 0px 16px 16px 16px; width: 568px; height:200px">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border: 1px solid #dadada; margin: 0; background-color: white; border-collapse: separate; table-layout: fixed; border-radius: 0px;">
                    <tbody>
                        <tr>
                            <td style="padding: 16px 16px 0px 16px; color: #535252 ">
                                <table role="presentation" border="0" width="100%" style="border-collapse: collapse;">
                                    <tbody><tr style="font-size: 12px">
                                        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; font-weight: bold; color: #535252">
                                            <a trackobject="" style="text-decoration: none; color: #535252;">
                                                City
                                            </a>
                                            <!--<img src="" iconthumbnail="clock.png" width="14" height="14" style="vertical-align: middle;">-->
                                        </td>
                                        <td align="right" style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; color: #535252">
                                            <!-- <a href="https://nordlo.sharepoint.com/sites/city/SitePages/Adminprotokoll-nu-utlagt-för-22-01-11.aspx?e=6atwwZmUu1prBP93zJbjcQAA6L-jYQAAAAA=_2_1_1_4_2" trackobject style="text-decoration: none; color: #535252;"> -->            Frequently visited                                            <!-- </a> -->
                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                        </tr>

                        <tr>
                            <td height="16" style="height: 16px"></td>
                        </tr>

                        <tr>
                            <td style="padding: 0px 16px">
                                <table role="presentation" border="0" width="100%" cellpadding="0" cellspacing="0" style="border-collapse: separate;">
                                    <tbody><tr style="display: flex;">
                                            <td valign="top" width="408" height="102" style="height: 102px; width: 408px;">
                                                <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; table-layout: fixed;">
                                                    <tbody><tr>
                                                        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; text-decoration: none; font-size: 16px; color: #303030; font-weight: bold; line-height: 19px;">
                                                            <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnordlo.sharepoint.com%2Fsites%2Fcity%2FSitePages%2FAdminprotokoll-nu-utlagt-f%25C3%25B6r-22-01-11.aspx%3Fe%3D6atwwZmUu1prBP93zJbjcQAA6L-jYQAAAAA%253d_2_1_1_4_2%26at%3D38&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=qamcXeRjHAaiu4k7kkHX2Ot6Va7rSld3E4wuEzpDt3A%3D&amp;reserved=0" originalsrc="https://nordlo.sharepoint.com/sites/city/SitePages/Adminprotokoll-nu-utlagt-f%C3%B6r-22-01-11.aspx?e=6atwwZmUu1prBP93zJbjcQAA6L-jYQAAAAA%3d_2_1_1_4_2&amp;at=38" shash="gHPYUf2s0e6sOHefihiBN1EbLHNhLvW9eWhLHoV2fyOxnK846qSBLfhaJUTuV6Lj6M19Gbt7jiGDXqAH7f2MfPfkVF5BEjspT0elQ3cCO0yvfx511Myvyawwv8ceSnI79k6BQwqz5Na3iYp+FngkuG/s+PFlm2CHuzEbIKqUBpY=" style="text-decoration: none; color: #303030;">
                                                                Adminprotokoll nu utlagt för 22-01-11
                                                            </a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td height="10" style="height:10px;"></td>
                                                    </tr>
                                                    <tr>
                                                        <td style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; line-height: 19px; font-size: 14px; color: black; -webkit-line-clamp: 3;display: -webkit-box;overflow: hidden;-webkit-box-orient: vertical;">

                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            </td>
                                            <td width="9" style="width:9px"></td>
                                            <td valign="top" style="vertical-align: top;">
                                                <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnordlo.sharepoint.com%2Fsites%2Fcity%2FSitePages%2FAdminprotokoll-nu-utlagt-f%25C3%25B6r-22-01-11.aspx%3Fe%3D6atwwZmUu1prBP93zJbjcQAA6L-jYQAAAAA%253d_2_1_1_4_2%26at%3D38&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=qamcXeRjHAaiu4k7kkHX2Ot6Va7rSld3E4wuEzpDt3A%3D&amp;reserved=0" originalsrc="https://nordlo.sharepoint.com/sites/city/SitePages/Adminprotokoll-nu-utlagt-f%C3%B6r-22-01-11.aspx?e=6atwwZmUu1prBP93zJbjcQAA6L-jYQAAAAA%3d_2_1_1_4_2&amp;at=38" shash="gHPYUf2s0e6sOHefihiBN1EbLHNhLvW9eWhLHoV2fyOxnK846qSBLfhaJUTuV6Lj6M19Gbt7jiGDXqAH7f2MfPfkVF5BEjspT0elQ3cCO0yvfx511Myvyawwv8ceSnI79k6BQwqz5Na3iYp+FngkuG/s+PFlm2CHuzEbIKqUBpY=" style="text-decoration: none;" aria-label="news link">

                                                    <img aria-hidden="true" width="120" style="width: 120px; display: block; border-radius: 0px;" alt="news thumbnail image" src="cid:17a3a2d7-a44a-46ea-9121-20c6c6c1f947" backupthumbnailsrc="https://nordlo.sharepoint.com/_api/v2.0/sharePoint:/sites/city/SitePages/Adminprotokoll-nu-utlagt-f%C3%B6r-22-01-11.aspx:/driveItem/thumbnails/0/c400x99999/content?preferNoRedirect=true&amp;prefer=extendCacheMaxAge&amp;clientType=modernWebPart">

                                                    <!-- Remove the code after fixing image height issue.
                                                        <img width="120" height="102" style="width: 120px; height: 102px; display: block; border-radius: 0px;" iconthumbnail="News.png" alt="" src="https://nordlo.sharepoint.com/_api/v2.1/sites/nordlo.sharepoint.com,100da8f8-16dd-431e-aee2-8571fa99e6ec,55d1cf66-5306-4851-ac81-26dfdfddc3b8/items/bfaa80d1-5be1-446c-a0dd-839c1c25a900/driveItem/thumbnails/0/c400x99999/content?Prefer=noredirect,closestavailablesize">
                                                    -->
                                                </a>
                                            </td>
                                    </tr>
                                </tbody></table>
                            </td>
                        </tr>

                        <tr>
                            <td height="16" style="height: 16px"></td>
                        </tr>

                        <tr>
                            <td style="padding: 0px 16px">
                                <table role="presentation" border="0" width="100%" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; table-layout: fixed; font-size: 12px; line-height: 16px; color: #535252;">
                                    <tbody><tr>
                                        <td>
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; table-layout: fixed;">
                                                <tbody><tr>
                                                    <td style="white-space: nowrap; font-size: 12px; line-height: 14px;font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; overflow: hidden; text-overflow:ellipsis; max-width: 357px; color: #535252">
                                                        Eric Rudblom
                                                        &nbsp;|&nbsp;&nbsp;
                                                    </td>
                                                    <td style="white-space: nowrap; font-size: 12px; line-height: 14px; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; color: #535252">
                                                        13 Jan, 2022
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        </td>
                                            <td align="right" style="vertical-align: bottom;">
                                                <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; border-spacing: 0; table-layout: fixed;">
                                                    <tbody><tr>
                                                        <td style="font-size: 12px; line-height: 14px; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; color: #535252">
                                                            <img src="cid:7c7d8b97-37d4-41ec-abac-5a144e0efab3" aria-hidden="true" alt="view icon" height="8" width="10">&nbsp;&nbsp; 3 views
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            </td>
                                    </tr>
                                </tbody></table>
                            </td>
                        </tr>

                        <tr>
                            <td height="16" style="height: 16px"></td>
                        </tr>
                    </tbody>
                </table>
            </td>
            <!--<![endif]-->
        </tr>

                                <!-- AutoNewsDigest Footer -->


    <tr>
        <td style="padding: 16px 0 32px 0;">
            <!-- Button : Begin -->
            <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin: auto;">
                <tbody><tr>
                    <td bgcolor="#1D3C34" style=" padding: 6px 17px; border: 1px solid #000000;border-radius: 0px;font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; font-size: 12px; text-decoration: none; display: inline-block;">
                        <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnordlo.sharepoint.com%2F_layouts%2F15%2Fsharepoint.aspx%3Fv%3Dnews%26e%3DYr88zdZ_FUiJ6V7VEmfMBA%26at%3D38&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=gu%2F5WpiLq4135qWM31dDrTKL1JtWZCIKpsFOKhrDcgU%3D&amp;reserved=0" originalsrc="https://nordlo.sharepoint.com/_layouts/15/sharepoint.aspx?v=news&amp;e=Yr88zdZ_FUiJ6V7VEmfMBA&amp;at=38" shash="cU8gD4WhGksghkHl1O0EPxbbk8i3lkJ65C/fKcDI2k6/A2wKaaAzH6BlI1+EX5VOvO3ZCQ2Kn90QSDgwHG6B+QjW5QFEycdwMHbBJgASoqXGhquS2fLMuofDl3cFdDMPJHxWaU2teqI/j90Pn6FlSGNI8tPwWbpIAPPad8Sir+I=" style="color:  #F3DBC6; text-decoration: none; " target="_blank">
                            See all news
                        </a>
                    </td>
                </tr>
            </tbody></table>
            <!-- Button : END -->
        </td>
    </tr>
    <tr>
        <td>
            <table role="presentation" border="0" style="font-size: 12px;width: 100%">
                <tbody><tr>
                    <td align="left" style="padding: 0px 14px 0px 14px; font-size:12px;line-height: 14px; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif;">
                        <a style="color: #000000; text-decoration: none; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif;" href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fprivacy.microsoft.com%2Fen-us%2Fprivacystatement&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=R9MgnGnQdG54YkU9Wa4pyrGWEW7ueY2hmiV7pdY1u2E%3D&amp;reserved=0" originalsrc="https://privacy.microsoft.com/en-us/privacystatement" shash="Qyxqcv3M+wM+MYZgr7F2PeKhGI25N+5sMbEHUEthK+HzjwgE1/C/m48bsHqgUKAzb8fOna4GXd+s8S8FjVEwJqYRmBOUd8mbgALaMCjv/CaBT+A4cYMnR8u4UJHZ3s9JYj45mXQ3tdOpPh7LERiQZKHvDUDQE43eavHzx34grKU=" target="_blank">Privacy Statement</a>
                        &nbsp;|&nbsp;
                            <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fnordlo.sharepoint.com%2F_layouts%2F15%2Fsharepoint.aspx%2FemailNotificationSettings&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=KT31VnOevEB2VTPOyXx5v6uvQQzRSAwUV8ST%2BzvJOD0%3D&amp;reserved=0" originalsrc="https://nordlo.sharepoint.com/_layouts/15/sharepoint.aspx/emailNotificationSettings" shash="gTBKHe8CIp+OcIFbOfNquyHRMPpkFjEbRiRfGMousHbWwV8RBPdi9MerRVlMzOKHkqYJus3mJqLsrIyZIVHn5RCuxc5LdONL/UGGYd+frHjVnklPW6mvFkk9EObAokFFNaEFygp+scHpSeTq/U4Hod+puGd0hIKHEDYYMMLNQDo=" style="color: #000000; text-decoration: none; ">Notification Settings</a>
                    </td>
                    <td align="right" style="padding: 0px 12px 0px 12px">
                        <table border="0" valign="right">
                            <tbody>
                                <tr>
                                    <td>
                                        <img src="cid:0ab2d97f-2695-4eab-b0d0-a80727243b43" aria-hidden="true" alt="mobile icon" style="width: 8px;height: 13px;vertical-align: middle;" height="14" width="8">
                                    </td>
                                    <td>
                                        <a href="https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fgetspmatmention&amp;data=04%7C01%7Ckevin.sundin%40nordlo.com%7Ce03c742ecc714b2823c908d9d8bc5211%7Cc23b3840812e40679bdba3eb446c5892%7C0%7C0%7C637779125611601578%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=WqxwZVIiH8%2Fm4QPop8sf9cfdze1uPvsJpvKEeKnR504%3D&amp;reserved=0" originalsrc="https://aka.ms/getspmatmention" shash="MzC3D+x5wmlihDkgATgLu8yLRqkeSmWuPR8cAiYAFm7j1/BlCmZG0Lt/aoWygWJdd2rt58GBaS+Y/jMtgZNft13o7GLFyo2rq5ikv/ZNZ384a8H1wT2kb0pLmBfqUffqgwzCYBiC0zNBwzwdvkMVVkv3/35oFy1LLDcQ8D0VjLE=" style="height:14px; text-align: right; line-height: 14px;font-size: 12px;font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', 'Helvetica Neue', sans-serif; padding: 0; margin: 0; height: 0px; text-decoration: none; color: #000000">
                                            &nbsp; Get the SharePoint Mobile App
                                        </a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
    <tr>
        <td style="height: 32px;"></td>
    </tr>
    <tr bgcolor="#1D3C34" style="height: 10px;">
        <td></td>
    </tr>

<!-- End Footer -->

                            </tbody>
                        </table>
                    </td>
            </tr>
        </tbody>
    </table>

<img src="https://northeuroper-notifyp.svc.ms:443/api/v2/tracking/method/View?mi=Yr88zdZ_FUiJ6V7VEmfMBA" aria-hidden="true" role="presentation" height="1" width="1" istrackingpixel="true"></body></html>
"""

    TO = 'kevinzundin@gmail.com'
    FROM = 'kevinzundin@gmail.com'

    py_mail("Test email subject", email_content, TO, FROM)
