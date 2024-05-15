# 1. Write a Python program to find leap year (user input)

year=int(input("Enter the year: "))
print("Leap year" if year%400==0 and year%100==0 or year%100!=0 and year%4==0 else  "Not a leap year")
