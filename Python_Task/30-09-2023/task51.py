# Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3


res=[i for i in range(10,51) if i%2!=0 and i%3!=0]
print(res)