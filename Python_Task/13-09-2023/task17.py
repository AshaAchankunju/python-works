# 1. Write a Python program that accepts a string and calculates the number of digits and letters.
word=input("enter the string:")
c_count=0
d_count=0

for w in word:
    if w.isdigit():
        d_count=d_count+1
    elif w.isalpha():
        c_count=c_count+1
print("character count= ",c_count)
print("digit count= ",d_count)


