from json import load
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\currency\\data.json",encoding="utf-8")
data=load(f)

source_curr=input("enter the sourcecurrency")
dest_curr=input("enter the destination currency")
amount=int(input("enter the amount"))

conversion_rate=data.get("conversion_rates")
# print(conversion_rate)

source_curr_code_rate=conversion_rate.get(source_curr)
dest_curr_code_rate=conversion_rate.get(dest_curr)
# print(source_curr_code_rate)
# print(dest_curr_code_rate)

current_rate=(amount/source_curr_code_rate)*dest_curr_code_rate
print(current_rate)

    
    

            
