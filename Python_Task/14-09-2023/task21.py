# 2.Write a python program to reverse the tuple
tup=(2,3,4,5,6,9,5)
print("Original Tuple Items = ", tup)
rev_tup = ()

for i in range(len(tup) - 1, -1, -1):
    rev_tup += (tup[i],)

print("Reverse tuple=",rev_tup)