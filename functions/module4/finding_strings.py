word = input("> ")
letter_list = "nabucodonosor"

the_word = ""
for letter in word:
    if letter in letter_list:
        the_word += letter

if the_word == word:
    print("yes")
else:
    print("no")
