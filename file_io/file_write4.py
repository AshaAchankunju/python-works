# read all years from years.txt and print leap years

path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\years.txt"

f=open(path,"r")
for line in f:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)