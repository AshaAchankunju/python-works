# validate date

from re import *

date=input("enter the month in ddmmyyyy: ")

rule="(0[1-9]|1[0-9]|2[0-9]|3[0-1])(0[1-9]|1[012])[0-9]{4}"

matcher=fullmatch(rule,date)
print("valid" if matcher!=None else "invalid")