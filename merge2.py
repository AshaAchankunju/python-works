str1=input("enter string1")
str2=input("enter strig 2")

smallest_length=min(len(str1),len(str2))
result=""

for i in range(0,smallest_length):
    out=str1[i]+str2[i]
    result+=out

if len(str1)>len(str2):
    rem=str1[smallest_length:]
else:
    rem=str2[smallest_length:]

result+=rem
print(result)