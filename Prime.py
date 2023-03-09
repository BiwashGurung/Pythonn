num = int(input("Enter a number ( greater than 1)"))  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The enter number is a PRIME number")
else:
    print("The enter number is not a prime number")
