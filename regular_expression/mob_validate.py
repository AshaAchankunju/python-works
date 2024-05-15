# indian mobile number validate

from re import *

ph_number=input("Enter mobile number: ")

rule="([+]91)?[0-9]{10}"
matcher=fullmatch(rule,ph_number)
print("valid" if matcher!=None else "invalid")