# validate years 1900-2099

from re import *

year=input("enter the year: ")

rule="(19|20)[0-9]{2}" # or (19[0-9]{2})|20[0-9]{2}
matcher=fullmatch(rule,year)
print("valid" if matcher!=None else "invalid")