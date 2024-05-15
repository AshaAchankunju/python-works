# print first recursive character
text="ABCABBDE"
charctercount={}

for ch in text:
    if ch in charctercount:
        print(ch)
        break
    else:
        charctercount[ch]=1
