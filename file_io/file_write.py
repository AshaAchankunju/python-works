path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\color.txt"
f=open(path,"w")

# f.write("hello") # in year.txt file


colors=["red","green","blue"]
for c in colors:
    f.write(c+"\n")