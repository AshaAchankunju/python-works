# 3.Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
for row in range(6,0,-1):
    for col in range(row):
        print(row,end=" ")
    print()