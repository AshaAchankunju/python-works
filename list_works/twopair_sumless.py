lst=[3,4,5,2,6]
sum=int(input("enter the sum="))
lst.sort()

low=0
upp=len(lst)-1
while(low<upp):
    curr_sum=lst[low]+lst[upp]
    if curr_sum==sum:
        print(lst[low],lst[upp])
        low+=1
        upp-=1
    elif curr_sum<sum:
        low+=1
    elif curr_sum>sum:
        upp-=1
