# start with kl
# 2 dugit
# 1 or two alphabet
# 4 digits

from re import *

variable_name=input("enter the variable")

rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}(-)?"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid")
