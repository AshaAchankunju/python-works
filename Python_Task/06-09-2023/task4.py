# 4.Write a program to find the largest number out of three numbers excepted from user.
num1=int(input("enter the 1st number="))
num2=int(input("enter the 2nd number="))
num3=int(input("enter the 3rd number="))
if(num1>num2 and num1>num3):
    print(f"largest is {num1}")
elif(num2>num1 and num2>num3):
    print(f"largest is {num2}")
elif(num3>num1 and num3>num2):
    print(f"largest is {num3}")