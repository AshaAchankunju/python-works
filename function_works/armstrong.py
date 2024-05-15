
def armstrong(num):
    dig_count=len(num)
    num=int(num)
    original=num
    sum=0
    while(num!=0):
        last_dig=num%10
        pow=last_dig**dig_count
        sum=sum+pow
        num=num//10
    return(True if sum==original else False)
print(armstrong("154"))