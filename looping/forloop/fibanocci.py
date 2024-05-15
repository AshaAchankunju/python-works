pre_num=0
curr_num=1
print(pre_num, end=" ")
print(curr_num, end=" ")
for i in range (1,11):
    next=pre_num+curr_num
    print(next, end=" ")
    pre_num=curr_num
    curr_num=next