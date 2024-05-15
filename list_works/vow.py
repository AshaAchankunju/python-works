list1=["red","green","blue","white","black","apple","ignore","under"]

vow=[name for name in list1 if name[0] in ["a","e","i","o","u"] ] 
print(vow)

cons=[name for name in list1 if name[0] not in ["a","e","i","o","u"] ] 
print(cons)