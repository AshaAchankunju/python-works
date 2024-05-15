lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)

# evens=[]
# for num in lst:
#     if(num%2==0):
#         evens.append(num)
# print(evens)

    #list comprehension
squares=[num**2 for num in lst]
print(squares)
cubes=[num**3 for num in lst]
print(cubes)
even=[num for num in lst if num%2==0 ]
print(even)
odd=[num for num in lst if num%2!=0 ]
print(odd)
nm_gt_five=[num for num in lst if num>5]
print(nm_gt_five)

c4=["anu","asha","ammu","appu"]
upper_name=[name.upper() for name in c4 ]
print(upper_name)

name_len_gt_four=[name for name in c4 if len(name)>2]
print(name_len_gt_four)

