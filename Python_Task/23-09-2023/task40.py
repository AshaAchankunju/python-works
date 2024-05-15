# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

for row in range(1,6):
    for i in range(1,row+1):
        print(i,end=" ")
    for col in range(row-1,0,-1):
        print(col,end=" ")
    print()