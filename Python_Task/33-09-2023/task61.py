# 2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out 
# anyone below a certain height.

dict={"john":156, "Manu":159, "Thomas":160, "Leo":145, "Henry":170,"Amir":158, "Steve":175}
for k,v in dict.items():
    if(v<170):
       print(k,v)
