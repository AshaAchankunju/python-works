arr=[4,9,5,6,9,5,4]
arr.sort()
count=1

i=0
while(i<len(arr)-1):
    j=i+1
    ith_elem=arr[i]
    jth_elem=arr[j]
    diff=jth_elem-ith_elem
    if diff==0:
        print(ith_elem)
        i=j
    i+=1
