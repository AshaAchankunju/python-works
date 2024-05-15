from re import *
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\regular_expression\\vehicle_number.txt","r")

rule="(KL|TN)-\d{2}-[A-Z]{2}-\d{4}"
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
        print(number)