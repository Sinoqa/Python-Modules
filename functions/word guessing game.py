word = "test"
guesses = " "

tries = 1
tries2 = 10


while tries <= 10:
    guess = input("Guess the word > ")
    guesses += guess + ", "
    tries += 1
    tries2 -=1
    if guess.lower() == word:
        print(f"congrats you got it on {tries - 1} tries ")
        print(f"Your guesses are {guesses}")
        break
    else:
        print(f"Try again, {tries2} remaining lives")
        print(f"current guesses are {guesses}")
        if tries2 == 0:
            print("insert a coin to try again")




