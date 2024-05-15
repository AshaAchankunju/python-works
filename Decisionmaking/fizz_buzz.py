#fizz buzz program

num=int(input("enter a number"))

if(num%15==0):
    print("fizz")
elif(num%5==0):
    print("buzz")
elif(num%3==0):
    print("fizz buzz")
else:
    print("not divisible by 3, 5,15")

