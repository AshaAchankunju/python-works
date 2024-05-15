# 2. Write a program to print sum of even number in a range
n1=int(input("enter first range: "))
n2=int(input("enter the last range: "))
sum=0
for num in range(n1,n2+1):
    if(num%2==0):
        sum=sum+num
print("sum=",sum)