# validate month
from re import *

month=input("enter the month in mm: ")

rule="(0[1-9]|1[012])"

matcher=fullmatch(rule,month)
print("valid" if matcher!=None else "invalid")