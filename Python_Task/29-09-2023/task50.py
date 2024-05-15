#  3. Pattern print 
#            1 1 1 1 1 1 1
#            2 2 2 2 2 2
#            3 3 3 3 3 
#            4 4 4 4 
#            5 5 5
#            6 6
#            7
for row in range(1,8):
    for col in range(8-row):
        print(row,end=" ")
    print()