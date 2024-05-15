# 1. Write a Python program that Use while loop to display elements from a given list present at odd index positions

num_list=[1,5,9,12,34,5,6]
i=1
while(i<len(num_list)):
    print("Elements at index position",i,"-",num_list[i])
    i+=2

