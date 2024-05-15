string1="ABC"
string2="PQR"

result=""

for i in range(0,len(string1)):
    out=string1[i]+string2[i]
    result+=out

print(result)