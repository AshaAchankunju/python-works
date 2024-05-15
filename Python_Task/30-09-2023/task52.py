# 2. Python program to check if the given string is a palindrome.

str=input("enter the string: ")
str_rev="".join(reversed(str))
if(str==str_rev):
    print("The string is a palindrome")
else:
    print("Not palindrome")