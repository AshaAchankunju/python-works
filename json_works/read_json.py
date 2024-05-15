from json import load
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\json_works\\students.json","r")
data=load(f)
print(data)

all_name= [emp.get("name")for emp in data]
print(all_name)

all_dept={dep.get("department")for dep in data}
print(all_dept)

max_sal=max(data, key=lambda d:d.get("salary"))
print(max_sal)