A = [
    [2, 3, 4],
    [1, 5, 6],
    [5, 8, 5]
]
num = len(A)
num = len(A[0])

diag = 0
above = 0
below= 0

max = A[0][0]
min = A[0][0]

for i in range(num):
    for j in range(num):
        if i == j: 
            diag += A[i][j]
        elif i < j: 
            above += A[i][j]
        else: 
            below += A[i][j]
        
        if A[i][j] > max:
            max = A[i][j]
        if A[i][j] < min:
            min = A[i][j]

print("Diagonal Sum: ", diag)
print("Above Diagonal Sum: ", above)
print("Below Diagonal Sum: ", below)
print("Max Element: ", max)
print("Min Element: ", min)