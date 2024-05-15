# Write a program to display ‘’HELLO’’ if a number entered by user is a multiple of five, otherwise print ‘’Bye’’.
# 2.Write a program to check whether a person is eligible for voting or not
# 3.Write a program to accept percentage from the user and display the grade according to the following criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade
# 4.Write a program to find the largest number out of three numbers excepted from user.

# num=int(input("enter the nmber: "))
# if num%5==0:
#     print("hello")                                        1
# else:
#     print("bye")

# age=int(input("enter your age"))
# if(age>=18):
#     print("eligible")                                     2
# else:
#     print("not eligible")

# mark=int(input("enter the mark in percentage: "))
# if mark>90:
#     print("A grade")                                      3
# elif mark<=90 and mark>80:
#     print("B grade")
# elif mark<=80 and mark>=60:
#     print("C grade")
# elif mark<60:
#     print("D grade")


# num1=int(input("enter the 1st number="))
# num2=int(input("enter the 2nd number="))                  4
# num3=int(input("enter the 3rd number="))
# if num1>num2 and num1>num3:
#     print(num1,"is the largest number")
# elif num2>num1 and num2>num3:
#     print(num2,"is the largest number")
# elif num3>num1 and num3>num2:
#     print(num3,"is the largest number")


# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

# 3. Take values of length and breadth of a rectangle from user and check if it is square or not.

# num1=int(input("enter the number"))
# num2=int(input("enter the second number"))
# opr=input("enter the operator")
# if(opr=="+"):
#     print("sum=",num1+num2)
# elif(opr=="-"):
#     if num1>num2:
#         print(num1-num2)
#     else:
#         print("ans=",num2-num1)

# age1=int(input("enter the age1"))
# age2=int(input("enter the age2"))
# age3=int(input("enter the age3"))
# if age1>age2 and age1>age3:
#     print("largest=",age1)
#     if age2>age3:
#         print("youngest=",age3)
#     else:
#         print("youngest=",age2)
# elif age2>age1  and age2>age3:
#     print("largest",age2)
#     if(age1>age3):
#         print(age3, "is youngest")
#     else:
#         print(age2, "is youngest")
# else:
#     print(age3,"is largest")
#     if(age1>age2):
#         print(age2,"is youngest")
#     else:
#         print(age1, "is youngest")
    

# length=int(input("enter the length "))
# breadth=int(input("enter the breadth "))

# if(length==breadth):
#     print("it is a square")
# else:
#     print("it is a rectangle")

# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10
# 2. Write a program to print sum of even number in a range
# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’’

# num=10
# while(num>=-10):
#     print(num)
#     num-=1

# sum=0
# for i in range(0,10):
#     if(i%2==0):
#         sum=sum+i
# print("sum=" , sum)

# weight=int(input("enter the weight in kg : "))
# height=int(input("enter the height in cm: "))
# # age=int(input("enter the age= "))
# height_m=height/100
# bmi=weight/(height_m**2)
# if(bmi<19):
#     print("underweight")
# elif(bmi>=19 and bmi<25):
#     print("Healthy")
# elif(bmi>20 and bmi<30):
#     print("overweight")


# 1.Write a python program to convert the temperature in degree centigrade to fahrenheit
# 2. Write a python program to find compound interest

# # 3. Write a python program to find area of a circle.

# .Write a python program to find factorial of a prime number
# 2.Write a python program to display Fibonacci series and specify that number odd or even
# 3.Write a python program to reverse digits in a number

# n=int(input("enter the number"))
# is_prime=True

# def fact(n):
#     fact=1
#     while n>=1:
#         fact=fact*n
#         n=n-1
#     return fact
# for i in range(2,n):
#     if(n%i==0):
#         is_prime=False
#         print("not prime")
#         break
# if is_prime==True:
#     result=fact(n)
#     print(result)
        


# first=0
# current=1
# print(first,"even")
# print(current,"odd")
# for i in range(1,10):
#     next=first+current
#     if next%2==0:
#         print(next,"even")
#     else:
#         print(next,"odd")
#     first=current
#     current=next

# 3.Pattern print
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for row in range(1,6):
#     for col in range(1,row+1):
#         print(row, end=" ")
#     print()

# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5
# for row in range(1,6):
#     for col in range(1,7-row):
#         print(row,end=" ")
#     print()

# 3.Pattern print 
#         * 
#       *   * 
#     *   *   * 
#   *   *   *   * 
# *   *   *   *   *

# for row in range(1,7):
#     for spc in range(7-row):
#         print(" ", end="")
#     for col in range(1,row):
#         print("* ", end="")
#     print()

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

# for row in range(1,6):
#     for col in range(1,6):
#         print("* ", end="")
#     print()

# 3.Pattern print 
#      * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
# #     *


# for row in range(1,7):
#     for spc in range(8-row):
#         print(" ", end="")
#     for col in range(1,row):
#         print("* ",end="")
#     print()
# for row in range(1,6):
#     for spc in range(row+1):
#         print(" ", end="")
#     for col in range(6-row):
#         print("* ",end="")
#     print()

#  Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# for row in range(1,7):
#     for col in range(1,row):
#         print(col , end=" ")
#     print()

# 3.Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# for row in range(1,7):
#     for col in range(7-row):
#         print(7-row,end=" ")
#     print()

# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

# -------------------------------------

# Write a program to display ‘’HELLO’’ if a number entered by user is a multiple of five, otherwise print ‘’Bye’’.
# num=int(input("enter the number= "))
# print("HELLO" if num%5==0 else "bye")

# Write a program to check whether a person is eligible for voting or not
# age=int(input("enter the age: "))
# print("eligible" if age>=18 else "not eligible")

# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# operator=input("enter the operator(-,+,*,/): ")
# if operator=="-":
#     print(f"result={num1-num2}")
# elif operator=="+":
#     print(f"result={num1+num2}")
# elif operator=="*":
#     print(f"result={num1*num2}")

# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10
# num=int(input("enter the limit"))
# while(num>=-10):
#     print(num,end=" ")
#     num=num-2

# 2. Write a program to print sum of even number in a range
# num1=int(input("enter the range1"))
# num2=int(input("enter the range2"))
# sum=0

# for i in range(num1,num2):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# 1.Write a python program to find factorial of a prime number
# num=int(input("enter the number"))
# is_prime=True

# def factorial(num):
#     fact=1
#     while(num>=1):
#         fact=fact*num
#         num=num-1
#     print(fact)
# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         print("not prime number")
#         break
# if is_prime==True:
#     print(factorial(num))

# 2.Write a python program to display Fibonacci series and specify that number odd or even

# num=int(input("enter the range "))
# first=0
# current=1
# print(first)
# print(current)
# for i in range(1,num):
#     next=first+current
#     print(next)
#     first=current
#     current=next
    
# 3.Write a python program to reverse digits in a number
# num=int(input("enter the number="))
# while(num!=0):
#     last_dig=num%10
#     num=num//10
#     print(last_dig,end="")

# 1. Write a Python program that accepts a string and calculates the number of digits and letters.

# num=input("enter the string")
# alpha_count=0
# num_count=0
# for i in num:
#     if i.isalpha():
#         alpha_count+=1
#     elif i.isdigit():
#         num_count+=1
# print("alpha_count=",alpha_count)
# print("num_count=", num_count)

# 3.Pattern print

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for row in range(1,6):
#     for col in range(0,row):
#         print(row,end=" ")
#     print("")


# 1. Write a Python program that separate positive and negative numbers from a list
# list=[-1,-2,5,6,-8]
# poslist=[]
# neglist=[]
# poslist=[num for num in list if num>0]
# neglist=[num for num in list if num<0]
# print(poslist)
# print(neglist)

# 2.Write a python program to reverse the tuple
# tup=(2,3,4,5,6,9,5)
# rev_tup=()
# for i in range(len(tup)-1,-1,-1):
#     rev_tup+=(tup[i],)
# print(rev_tup)


# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5

# for row in range(1,6):
#     for col in range(row,6):
#         print(row,end=" ")
#     print("")


# # 1. Write a Python program to find n natural number in ascending order
# n=int(input("enter the number:"))
# def natural(n):
#     if n<=0:
#         print("enter a natural number")
#         return
#     nat_um=[]
#     for i in range(1,n+1):
#         nat_um.append(i)
#     return nat_um
# print(natural(n))


# 3.Pattern print 
#         * 
#       *   * 
#     *   *   * 
#   *   *   *   * 
# *   *   *   *   *

# for row in range(1,6):
#     for spc in range(6-row):
#         print(" ",end="")
#     for col in range(1,row+1):
#         print("* ", end=" ")
#     print(" ")

# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

# for row in range(1,6):
#     for spc in range(6-row):
#         print(" ",end=" ")
#     for col in range(1,row+1):
#         print("* ",end="")
#     print()

#  1. Write a Python program to find leap year (user input)

# year=int(input("enter the year: "))
# if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#     print("leap year")
# else:
#     print("not leap year")


# # 2.Write a python program to sum all the items in the dictionary
# dict={"asha":5,"fdg":50,"mkj":58}
# print(sum(dict.values()))

# 3.Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

# for row in range(1,6):
#     for col in range(1,6):
#         print("* ",end="")
#     print()







