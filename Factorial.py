N = int(input("Enter a non-negative integer: "))


factorial = 1
counter = N


while counter > 0:
    factorial *= counter
    counter -= 1


print(f"{N}! = {factorial}")
