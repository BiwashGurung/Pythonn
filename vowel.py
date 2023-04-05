randomword = input('Enter a word:') #randomword = 'hello'
def vowel_consonant_count(word): #word = 'hello'
    word = word.lower()
    word = list(word)
    vowel_count = 0
    consonant_count = 0
    vowel_words = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] in vowel_words:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count

vcount, ccount = vowel_consonant_count(randomword)
print('total vowels are:', vcount)
print('total consonants are :', ccount)