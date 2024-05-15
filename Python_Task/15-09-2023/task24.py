# 2.Write a python program to find n natural number in descending order

number=int(input("Enter the number:"))
num=[]
for n in range(0,number+1):
    num.append(n)
num.reverse()
print("descending order=", num)