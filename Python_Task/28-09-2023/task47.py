# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E
i=65
for row in range(1,6):
    for col in range(1,row+1):
        print(chr(i),end=" ")
    print()
    i+=1

i=65
for row in range(1,6):
    for col in range(1,row+1):
        print(chr(i),end=" ")
    print("")
    i+=1