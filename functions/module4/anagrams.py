word1 = str(input('word 1 >'))
word2 = str(input('word 2  >'))
letters1 = []
letters2 = []
for letter in word1.lower():
   letters1.append(letter)
for letter in word2.lower():
   letters2.append(letter)
letters1.sort()
letters2.sort()
if letters1 == letters2:
   print("Anagram")
else:
   print("Not anagrams")

