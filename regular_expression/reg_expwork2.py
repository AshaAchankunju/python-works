from re import *

variable_name=input("enter the variable")

rule="[k-nK-N][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid")
