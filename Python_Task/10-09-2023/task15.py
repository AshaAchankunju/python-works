# 2.Write a python program to display Fibonacci series and specify that number odd or even
prev_num=0
curr_num=1
num=int(input("enter the limit="))
for i in range(1,num):
    next=prev_num+curr_num
    if next%2==0:
        print(next,"- even")
    else:
        print(next,"-odd")
    prev_num=curr_num
    curr_num=next





