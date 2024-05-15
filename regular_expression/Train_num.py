from re import *
f=open("C:\\Users\\sachi\\OneDrive\Desktop\\my python works\\regular_expression\\Train_num.txt","r")
rule="[0-9]{5}"
for line in f:
    train_info=line.split(" ")
    # print(train_info)
    for num in train_info:
        matcher=fullmatch(rule,num)
        if matcher!=None:
             print(num)


# or

# from re import *
# f=open("C:\\Users\\sachi\\OneDrive\Desktop\\my python works\\regular_expression\\Train_num.txt","r")
# rule="[0-9]{5}"
# for line in f:
#     words=line.rstrip("\n")
#     matcher=finditer(rule,words)
#     for m in matcher:
#         print(m.group())
