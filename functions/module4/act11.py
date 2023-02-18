userWord = input("Enter a Word: ")
userWord = userWord.upper()
vowel = ["A","E",'I','O','U']
for letters in userWord:
    if letters in vowel:
        continue
    print(letters)
