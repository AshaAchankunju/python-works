path="C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\file_io\\century_year.txt"

f=open(path,"w")

# start_year=1800
# end_year=2024
# while(start_year<=end_year):
#     if(start_year%100==0):
#         f.write(str(start_year)+"\n")
#     start_year+=1

#     or

for year in range(1800,2024):
    if(year%100==0):
        f.write(str(year)+"\n")