n1=int(input("enter the number"))
n2=int(input("enter the sec number"))

small_num= n1 if n1<n2 else n2
i=1
while(i<=small_num):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i+=1

print(f"gcd if numbers is{gcd}")
lcm=(n1*n2)/gcd
print(f"lcm of numbers is {lcm}")