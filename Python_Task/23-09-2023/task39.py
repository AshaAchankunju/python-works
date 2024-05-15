# 2.Write a python program that Take input from user and make square list of the number
#  and the cube list .Range is 10 number in the list

num_list=[]
sqr_list=[]
cub_list=[]
while len(num_list)<10:
    n=int(input("enter the number"))
    num_list.append(n)

sqr_list=[n**2 for n in num_list]
cub_list=[n**3 for n in num_list]
print("square list of the numbers= ",sqr_list)
print("cube list of the numbers =",cub_list)