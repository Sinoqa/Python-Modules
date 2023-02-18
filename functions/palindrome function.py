def palindrome(word):
    rev = ''.join(reversed(word))
    no_space_rev = rev.lower().replace(' ','')
    if no_space_rev == word:
     return True
    else:
        return False

word = str(input("> "))
lower_word = word.lower().replace(' ','')
rev_word = palindrome(lower_word)

if rev_word:
   print("It's a palindrome")
elif rev_word == False:
   print("It's not a palindrome")
