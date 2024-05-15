# 1. Write a Python program that separate positive and negative numbers from a list

lst=[1,2,3,4,5,-6,-8,-7,9]
postv_intgr=[]
negtv_intgr=[]

postv_intgr=[num for num in lst if num>0 ]
negtv_intgr=[num for num in lst if num<0]
print(postv_intgr)
print(negtv_intgr)