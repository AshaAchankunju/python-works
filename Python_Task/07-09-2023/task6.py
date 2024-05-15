# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input("Enter 1st person age: "))
age2=int(input("Enter 2nd person age: "))
age3=int(input("Enter 3rd person age: "))

if(age1>age2 and age1>age3):
    print(f"{age1} is Oldest ")
elif(age2>age3 and age2>age1):
    print(f"{age2} is oldest")
else:
    print(f"{age3} is oldest")

if(age1<age2 and age1<age3):
    print(f"{age1} is youngest")
elif(age2<age3 and age2<age1):
    print(f"{age2} is youngest")
else:
    print(f"{age3} is youngest")





# if(age1>age2 and age1>age3):
#     print(f"{age1} is Oldest ")
# else:
#     print(f"{age1} is youngest ")
# if(age2>age3 and age2>age1):
#     print(f"{age2} is oldest")
# else:
#     print(f"{age2} is youngest")
# if(age3>age1 and age3>age2):
#     print(f"{age3} is Oldest")
# else:
#     print(f"{age3} is youngest")