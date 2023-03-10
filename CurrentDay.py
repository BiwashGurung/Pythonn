x=str(input("Enter today's day : "))
x=x.lower()
if(x=="saturday"):
    print("Enjoy your weekend!")
elif(x=="sunday" or x=="monday" or x=="wednesday" or x== "thursday" or x=="friday"):
    print("Happy weekday! Work hard!")
else:
    print("Invalid week day")