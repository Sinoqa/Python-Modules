#for loops

secret_number = 777
print('''
+================================
|Welcome to my game, muggle!    |
|Enter an integer number        |
|and gues what number I've      | 
|picked for you.                |
|So, what is the secret number? |
+================================''')
while True:
    guess = int(input("guess > "))
    if guess != secret_number:
        print("Ha ha! You're stuck in my loop!")
    else:
        print("Well done, mumggle! You are free now.")
        break
