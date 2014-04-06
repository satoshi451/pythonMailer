#coding=utf8
# "evgil@mail.ru"

import smtplib

from email import Encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart

"""
class contact():
    def __init__(self, sName, fName, surname, email):
        self.secondName = sName[1:len(sName)-1]
        self.firstName = fName[1:len(fName)-1]
        self.surname = surname[1:len(surname)-1]
        self.email = email[1:len(email)-1]

    def toString(self):
        return "sName: " + self.firstName + "; fName: " + self.secondName + "; surName: " + self.surname + "; email: " + self.email

"""

emails_file2 = open("getEmails/cnt.txt", "rU")
addresses = []
emails = []

for line in emails_file2.readlines():
    if line[0:len(line)-1] not in addresses and line[0:len(line)-1] != '':
        addresses.append(line[0:len(line)-1])

#addresses = ['evgil@mail.ru']#, 'votrin-banan@mail.ru']
#addresses = ['votrin.and@yandex.ru']
print(addresses)
print len(addresses)
exit(1)

"""
for line in emails_file2.readlines():
    tmpStr = line.split()
    tmpContact = contact(tmpStr[1], tmpStr[2], tmpStr[3], tmpStr[4])
    addresses.append(tmpContact.email)
"""

emails_file2.close()

me = 'From: wiseman'
you = 'To: ' + ', '.join(addresses)

server = 'smtp.gmail.com'
port = 25
user_name = 'mokusai92'
user_passwd = 'Ns5(!11PLus'

msg = MIMEMultipart('mixed')
msg['Subject'] = 'Наши программы.'
msg['From'] = me
msg['To'] = ' '

htmlFile = open("html/tableHtml1.html", "rU")

htmlFile = htmlFile.read()

part1 = MIMEText(htmlFile, 'html')
#!!!!
part1.set_charset('utf-8')

msg.attach(part1)
#-----------------------------------------------------------------------------------------------------------------------
# add attach file1
part = MIMEBase('application', "octet-stream")
filename = "C:\Users\wiseman\PycharmProjects\mails\Marafon_new.doc"

part.set_payload(open(filename, "rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'Подробности о программе МАРАФОН.doc')
msg.attach(part)
#-----------------------------------------------------------------------------------------------------------------------
# add attach file
part = MIMEBase('application', "octet-stream")
filename = "C:\Users\wiseman\PycharmProjects\mails\SP_new.docx"

part.set_payload(open(filename, "rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'Подробности о программе СИНЕРГИЯ.doc')
msg.attach(part)
#-----------------------------------------------------------------------------------------------------------------------
#exit(2)

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)

s.sendmail(me, addresses, msg.as_string())
s.quit()

"""

#imgWoman = open("img/woman.jpg", "rb")
#attWoman = MIMEImage(imgWoman.read())
#imgWoman.close()
#attWoman.add_header('Content-ID', '<woman>')

#imgRose = open("img/rose.jpg", "rb")
#attRose = MIMEImage(imgRose.read())
#imgRose.close()
#attRose.add_header('Content-ID', '<rose>')

#msg.attach(attWoman)
#msg.attach(attRose)

"""