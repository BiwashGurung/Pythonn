arr = [1, 2, 3, 4, 5, 6]
arr1=[]

for i in range(len(arr)-1, -1, -1):
    ele = arr[i]
    arr1.append(ele)

print(arr1)
