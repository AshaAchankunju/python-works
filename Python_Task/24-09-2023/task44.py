# 4.Pattern print 
#         A 
#        B C 
#       D E F 
#      G H I J 
# #     K L M N O
i=65
for row in range(1,6):
    for spc in range(6-row):
        print(" ",end=" ")
    for col in range(1,row+1):
        print(f"{chr(i)} ",end="  ")
        i+=1
    print()
