from re import *
text="aaaabcaabbaaaaabd"

# pattern="a*" # any number of a including  0 numbers
pattern="a{2}" # 2 numbers of a 
matcher=finditer(pattern, text)
count=0
for m in matcher:
    print (m.start(),m.group())
    count+=1
print(count)