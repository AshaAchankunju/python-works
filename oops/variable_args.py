# def addition(*args):
#     return sum(args)

# print(addition(10,20,30))
# print(addition(10,20,45,58))

# last digit sum

# def add(*args):
#     sum=0
#     for a in args:
#         n=a%10
#         sum=sum+n
#     return sum
# print(add(140,254,154))

# last digit max

# def last_dig_maxm(*args):
#     dig=[(a%10) for a in args ]
#     return max(dig)
# print(last_dig_maxm(12,15,16))


# def add_emp(*args):
#     print(args)
# add_emp(10,20,"vdvv","dghgdgd")

# def add_emp(**kwargs):
#     print(kwargs)
#     print(kwargs.get("name"))
# add_emp(id=10,name="asha",location="tvm")

# def last_dig_sort(*args, **kwargs):
#     digit=[n%10 for n in args]
#     value=kwargs.get("reversed")
#     if value==True:
#         digit.sort(reverse=True)
#     else:
#         digit.sort()
#     return digit
# print(last_dig_sort(10,15,14,32,reversed=True))


# last_digit_calculator(432,456,584,654,op=)
def last_digit_calc(*args,**kwargs):
    digit=[n%10 for n in args]
    operator=kwargs.get("operator")
    if operator=="+":
        total=sum(digit)
    elif operator=="*":
        total=1
        total=total*digit
    return total
print(last_digit_calc(11,12,13,operator="+"))
    

