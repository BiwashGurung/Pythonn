arr = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6] 
arr1=[]

for i in range(len(arr)-1, -1, -1):
    ele = arr[i]
    if ele not in arr1:
        arr1.append(ele)

print(arr1)
