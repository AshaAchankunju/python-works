# 1. Write a Python program that ask users to enter a number and keep asking the users 
# to enter a correct number, until the number with in the range that we given

  
num=int(input("enter a number within 1 and 20: "))
while True:
    if num in range(1,20):
        print("correct number")
        break
    else:
        new_num=int(input("enter the correct numer:"))  
    num=new_num





    # num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# num=int(input("enter the number: "))
# while True:
#     if num not in num_list:
#         new_num=int(input("enter the correct numer:"))
#         num=new_num
#     else:
#         print("correct number")
#         break