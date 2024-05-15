#  2. Write a python program to make combinations of 3 digits
list=[1,2,3]
comb_list=[]

for i in list:
    for k in list:
        for j in list:
            comb_list.append([i,j,k])
print(comb_list)

