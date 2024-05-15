# 3. Write a program to handling missing keys
dict={1:"apple",2:"orange",3:"mango"}
ky=int(input("enter the key to search="))

if ky in dict.keys():
    print("key found")
else:
    print("key not foud")