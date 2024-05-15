employee={"id":1000,"name":"Manu","position":"developer"}
print(employee)

employee["department"]="Software developer"
print(employee)

# if salary not present add salary as 450000 if present add 10000 to the existing salary
if "salary" not in employee:
    employee["salary"]=450000
else:
    employee["salary"]+=10000
print(employee)