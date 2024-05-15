# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

for row in range(6):
    for spc in range(6-row-1):
        print(" ", end="")
    for col in range(2*row+1):
        if col==0 or col==2*row:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for row in range(6-2,-row,-1):
    for spc in range(6-row-1):
        print(" ",end="")
    for col in range(2*row+1):
        if(col==0 or col==2*row):
            print("*", end="")
        else:
            print(" ",end="")
    print()