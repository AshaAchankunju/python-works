# read numbers file and return valid phone number
from re import *
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\regular_expression\\numbers.txt","r")
rule="([+]91)?[0-9]{10}"
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
        print(number)