start_year=int(input("enter the start year"))
cur_year=2023
i=start_year

while(i<=cur_year):
    year=i
    if(year%100==0 and year%400==0 or year%100!=0 and year%4==0):
        print(year) 
    i+=1    