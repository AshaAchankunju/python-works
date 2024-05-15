#     3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E
i=65
for row in range(5):
    for spc in range(5-row-1):
        print(" ", end="")
    for col in range(row+1):
        print(chr(i+col) , end=" ")
    print("")
    
i=65
for row in range(5):
    for spc in range(5-row-1):
        print(" ",end="")
    for col in range(row+1):
        print(chr(i+col),end=" ")
    print("")

