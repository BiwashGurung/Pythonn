l = [5,1,4,2,8]

def bubble_sort(arr):
    n = len(arr)
   
    for i in range(2):
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubble_sort(l)
print(l)
