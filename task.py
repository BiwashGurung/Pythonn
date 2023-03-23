ask = True
arr = []
while ask == True:
    arr.append(int(input("Please enter a number :" )))
    a = input("Do you want to keep on entering number :" )
    if a == "No" or a == "n":
        ask = False

print ("ThankYou for Submission")