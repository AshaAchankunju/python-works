# 2.Write a python program to accept decimal number and display it’s binary number
n=int(input("enter a decimal number: "))
binary=""
while n>0:
    binary=str( n % 2) + binary
    n=n//2
print(binary)   
