import smtplib
import imaplib
import email
import getpass
from  email.mime.text import MIMEText


MY_ID = input("ID : ")
MY_PASSWORD = getpass.getpass('PASSWORD : ')

while 1:
    MODE = input("Mode( send | receive | quit ) : ")

    if MODE == 'send':
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(MY_ID, MY_PASSWORD)
        res_name = input("TO: ")
        subject = input("SUBJECT: ")
        message = input("MESSAGE : ")
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = MY_ID
        msg['To'] = res_name
        smtp.sendmail(MY_ID, res_name, msg.as_string())
        print("Done!")
        smtp.quit()

    elif MODE == 'receive':
        imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        imap.login(MY_ID, MY_PASSWORD)
        imap.select('inbox')
        result, data = imap.uid('search', None, "ALL")
        latest_email_uid = data[0].split()[-1]
        result, data = imap.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email.decode('utf-8'))
        f = open("recent email.html", 'w')

        if email_message.is_multipart():
            for p in email_message.get_payload():
                f.write(p.get_payload())

        print("Done!")

        f.close()
        imap.close()
        imap.logout()
    elif MODE == 'quit':
        break
    else:
        print("Wrong Access")




