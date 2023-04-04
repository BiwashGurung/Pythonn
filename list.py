m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))


arr = [[0 for j in range(n)] for i in range(m)]


for i in range(m):
    for j in range(n):
        if i == j:
            arr[i][j] = 1
        elif i < j:
            arr[i][j] = 2
        else:
            arr[i][j] = 3


for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()