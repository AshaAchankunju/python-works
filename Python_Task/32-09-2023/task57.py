# Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers
num = [-1, 0, 1, 2, -1, -4,5,-5]
resu=[]
num.sort()
r=len(num)-1
for i in range(len(num)-2):
    l=i+1
    while(l<r):
        sum=num[i]+num[l]+num[r]
        if sum<0:
            l=l+1
        elif(sum>0):
            r=r-1
        elif not sum:
            resu.append([num[i],num[l], num[r]])
            l=l+1
print(resu)