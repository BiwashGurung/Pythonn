Name=input("Ener students name:")
Marks=0
for i in range(5):
    a=float(input("Enter the MArks obtained :"))
    Marks=Marks+a

average=int(Marks)/5
if(average>=70 and average<=100):
    grade="A"
elif(average>=60 and average <=69):
    grade="B"
elif(average>=50 and average<=59):
    grade="C"
elif(average>=43 and average <=49):
    grade="D"
elif(average>40 and average<=42):
    grade="E"
else:
    grade="F"

print("The grades obtained by" + str(Name) + " " + "is " + " " +str(grade)+".")
