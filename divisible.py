a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]

for i in range(len(a)):

    if a[i]% 2 ==0 and a[i] % 3 ==0:
        print(a[i],'the element is divisible by 2 and 3')