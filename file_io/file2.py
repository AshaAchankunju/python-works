f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\news.txt", "r")
sum=0
for line in f:
    words=line.rstrip("\n").split(" ")
    sum=sum+len(words)
print(sum)

# Total number of words

