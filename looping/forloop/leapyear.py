i=1800
j=2024
for year in range(i, j):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)