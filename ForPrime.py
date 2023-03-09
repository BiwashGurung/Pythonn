n = int(input('enter any number'))
prime = True

for i in range(2, n):
    r = n % i
    if r == 0:
        prime = False
        break

if prime:
    print('the number is prime')
else:
    print('the number is not prime')