n = int(input("Enter the number: "))


arr = []


for i in range(5):
    num = int(input("Enter number " + str(i+1) + ": "))
    arr.append(num)


sum_odd = 0
sum_even = 0

for i in arr:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers :", sum_odd)