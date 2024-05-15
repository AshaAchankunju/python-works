# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

source_list=[1, 3, 5, 1, 3, 2, 5, 4, 2]
sort=sorted(source_list)
result = []
 
for i in sort:
    found = False
    for j in range(len(result)):
        if i in result[j]:
            result[j].append(i)
            found = True
            break
    if not found:
        result.append([i])
print("Matrix after grouping : " , str(result))


        
