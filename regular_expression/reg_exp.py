from re import *

text="fat-cat-run-fast-catch"
pattern="at"

matcher=finditer(pattern,text)

count=0
for obj in matcher:
    print(obj.start(), obj.group())
    count+=1
print(count)
