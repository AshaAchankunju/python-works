def oneth_dig_smallest(num1,num2):
    a=num1%10
    b=num2%10
    res=num1 if a<b else num2
    return res
print(oneth_dig_smallest(15,16))