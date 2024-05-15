from re import *

variable_name=input("Enter the PAN Number: ")

rule="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"
matcher=fullmatch(rule,variable_name)
print("invalid"if matcher==None else " valid")