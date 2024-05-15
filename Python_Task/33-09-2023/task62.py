# 3. Pattern print 
#                             4 4 4 4 4 4 4  
#                             4 3 3 3 3 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 2 1 2 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 3 3 3 3 4   
#                             4 4 4 4 4 4 4


for row in range(0,7):
    for col in range(0,7):
        print(max(4-min(row,col,6-row,6-col),1), end="")
    print()











 
for row in range(1, 5): 
    for col in range(1, 5): 
        min = row if row < col else col 
        print(4 - min + 1, end = " ") 
 
    for col in range(3, 0, -1): 
        min = row if row < col else col
        print(4 - min + 1, end = " ")
 
    print()
     
for row in range(3, 0, -1): 
    for col in range(1, 5): 
        min = row if row < col else col 
        print(4 - min + 1, end = " ") 
 
    for col in range(3, 0, -1): 
        min = row if row < col else col 
        print(4 - min + 1, end = " ")
 
    print()