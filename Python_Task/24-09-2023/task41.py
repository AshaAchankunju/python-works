# 1. Write a python program to create a list of tuples having first element 
# as the number and second element as the cube of the number
num_list=[1,2,3,4,5,6,7]
cube_list=[(num,num**3)for num in range(1,len(num_list)+1)]
print(cube_list)
    
