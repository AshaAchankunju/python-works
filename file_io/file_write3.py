path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\years.txt"

f=open(path,"w")

for year in range(1800,2025):
    f.write(str(year)+"\n")