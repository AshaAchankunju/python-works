f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\news.txt", "r")
wc={}

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)