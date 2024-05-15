# validate date

from re import *

date=input("enter the date: ")

rule="(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[012])-(19|20)[0-9]{2}"

matcher=fullmatch(rule,date)
print("valid" if matcher!=None else "invalid")



