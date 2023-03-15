arr = [4,5,7,9,2]



numbers = []


for i in range(n):
    number = int(input("Enter an integer: "))
    numbers.append(number)


max_number = numbers[0]
min_number = numbers[0]


for number in numbers:
    if number > max_number:
        max_number = number
    elif number < min_number:
        min_number = number


print("The list of numbers is:", numbers)
print("The maximum number is:", max_number)
print("The minimum number is:", min_number)

