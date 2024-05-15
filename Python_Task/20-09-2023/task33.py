# 2.Write a python program to find the least square number from a list

list=[5,2,6,9,7]
lst_sqr=[]
for num in list:
    square=num**2
    lst_sqr.append(square)
sqrt_sorted=sorted(lst_sqr)
print(sqrt_sorted[0])

# import math
# list1=[15,26,30,35]
# s=[math.sqrt(ch)//1 for ch in list1 if ch>0]
# print("least square number for the list= ",s)
# lst_sqr_list=sorted(s)
# print("least square number=", lst_sqr_list[0])
    
