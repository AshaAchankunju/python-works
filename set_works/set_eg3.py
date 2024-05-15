order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","man","upuma","vegmeals","idly"}

# set2=order1.union(order2)
# print(set2)

# set3=order1.intersection(order2)
# print(set3)

# new_order=set2-set3
# print(new_order)

# new_order=order1.symmetric_difference(order2)
# print(new_order)

order1.update(order2)
print(order1)

