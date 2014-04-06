#coding=utf8
__author__ = 'wiseman'
from email import *


fileT = open("getEmails/contacts.txt", "r")


class contact():
    def __init__(self, sName, fName, surname, email):
        self.secondName = sName[1:len(sName)-1]
        self.firstName = fName[1:len(fName)-1]
        self.surname = surname[1:len(surname)-1]
        self.email = email[1:len(email)-1]

    def toString(self):
        return "sName: " + self.firstName + "; fName: " + self.secondName + "; surName: " + self.surname + "; email: " + self.email


for line in fileT.readlines():
    tmpStr = line.split()
    tmpContact = contact(tmpStr[1], tmpStr[2], tmpStr[3], tmpStr[4])
    print (tmpContact.toString())

fileT.close()


