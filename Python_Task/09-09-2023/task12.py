# 2. Write a python program to find compound interest

p=int(input("enter principal amount: "))
interest_rate=int(input("enter the interest rate in %: "))
r=interest_rate/100
t=int(input("enter the time period in years: "))
n=int(input("enter the no: of times interest compunded per year: "))

compound_interest=(p*(1+r/n)**(n*t))-p
print("compound interest= ",compound_interest)