text="hello hai hello hai"
wc={}
words=text.split()
print(words)

for ch in words:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

print(wc)
