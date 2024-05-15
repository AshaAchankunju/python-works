# 3.Write a python program to reverse digits in a number
num=int(input("enter the number="))
while(num!=0):
    last_digit=num%10
    num=num//10
    print(last_digit,end="")
