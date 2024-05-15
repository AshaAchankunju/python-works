# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

first_num=int(input("Enter 1st number: "))
second_num=int(input("Enter 2nd num: "))
operation=input("Enter operator")

if (operation=="+"):
    result=first_num+second_num
    print(result)
elif (operation=="-"):
    result=first_num-second_num
    print(result)
elif(operation=="*"):
    result=first_num*second_num
    print(result)
elif(operation=="/"):
    result=first_num/second_num
    print(result)