
read_path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\years.txt"
write_path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\leap_year.txt"
fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")