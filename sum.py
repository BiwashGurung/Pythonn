user = input("Enter a string of numbers: ")

sum = 0

for char in user:
  sum += int(char)

print("The sum of the numbers is:", sum)