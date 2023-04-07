word = input("Enter any word:")

word = list(word)

arr = []

for i in range( len(word)-1,-1,-1):
    arr.append(word[i])

print(arr)

if word == arr:
    print("The word is palindrome")
else :
    print ("the word is not palindrome")
