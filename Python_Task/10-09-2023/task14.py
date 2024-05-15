# 1.Write a python program to find factorial of a prime number

num=int(input("enter the number"))
is_prime=True

def factorial(num):
    fact=1
    while(num>=1):
        fact=fact*num
        num=num-1
    return(fact)
for i in range(2,num):
    if num%i==0:
        is_prime=False
        print(f"{num} is not prime")
        break
if(is_prime==True):
    result= factorial(num)
    print(f"{num} is prime number, factorial={result}")
    
    


# num=int(input("enter the nu:"))
# is_prime=True
# fact=1

# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# if(is_prime):
#     n=1
#     while(n<=num):
#         fact=fact*n
#         n=n+1
#     print("factorial=",fact)
# else:
#     print(num,",is not prime")

        
        
# num=int(input("enter the number"))
# is_prime=True
# fact=1

# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
# if(is_prime==True):
   
#     while(num>=1):
#         fact=fact*num
#         num=num-1
#     print(f"factorial={fact}")

# else:
#     print(num,"is not prime")