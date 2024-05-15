arr=[4,9,5,6,9,5,4]
arr.sort()
count=1

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        ith_elem=arr[i]
        jth_elem=arr[j]
        diff=jth_elem-ith_elem
        if diff==0:
            print(ith_elem)
            break
        count+=1

print(f"count={count}")