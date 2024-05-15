# 2.Write a python program to list the even numbers from the range that given by
# the user and delete the multiplication of 5 from the list


start=int(input("enter the starting range: "))
end=int(input("enter the end range: "))

even_num=[num for num in range(start,end+1) if num%2==0 ]
final_list=[n for n in even_num if(n%5!=0)]
print("list of even numbers= ",even_num)
print("Final_result= ",final_list)