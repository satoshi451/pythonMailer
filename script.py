#coding=utf8
"""
import re

__author__ = 'wiseman'

fileWoman = open('getEmails/women.txt', 'rU')
fileMan = open('getEmails/men.txt', 'rU')

fullFileWoman = fileWoman.read()
fullFileMan = fileMan.read()

print fullFileMan

pattern = re.compile('[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}')

print pattern.match(fullFileMan)

fileWoman.close()
fileMan.close()
"""


import re
text2 = "� ���⫠��, 28, 9037872776, kalibrisv@mail.ru, ����.jpg"
pattern = r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
number_re = re.compile(pattern)

fileT = open('getEmails/women.txt', 'rU')
text = fileT.read()

print text2

if number_re.findall(text2):
    print "Email of correct:"
else:
    print "Error:"

