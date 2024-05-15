# 1. Write a Python program that keep on accepting number from the user until users enter zero display 
# the sum of all number


sum=0
while(True):
    num=int(input("enter the number : "))
    if(num==0):
        break
    sum=sum+num
print("sum=",sum)
        

    
