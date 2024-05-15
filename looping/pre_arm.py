num=123
sum=0
while(num!=0):
    digit=num%10
    dig_cube=digit**3
    sum=sum+dig_cube
    num=num//10

print(sum)