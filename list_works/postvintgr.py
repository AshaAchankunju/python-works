arr=[1,4,3,5,6,7]

arr.sort()

i=0
while(i<len(arr)-1):
    j=i+1
    ith_elem=arr[i]
    jth_elem=arr[j]
    diff=jth_elem-ith_elem
    if diff!=1:
        missing_num=ith_elem+1
        i=j
    i+=1