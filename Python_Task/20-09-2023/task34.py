# 1. Write a Python program that print 2 list and common element

lst1=[1,2,3,4,5]
lst2=[3,4,5,6,7,8,9]
common_element=[]
print(f"list_1={lst1} list_2={lst2}")
for ch in lst1:
    if ch in lst1 and ch in lst2:
        common_element.append(ch)
print("common elements= ",common_element)
