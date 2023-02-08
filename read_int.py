
def readint(prompt, min, max):
    status = False
    while status != True:
        try:
            prompt = int(input(f"Enter a number from -10 to 10 "))
            if prompt in range(min, max):
                status=True
                v = prompt
                print("The number is:", v)
            if prompt < min or prompt > max:
                print(f"Error: The value is not within permitted range {min}..{max}")
        except ValueError:
            print("Error: wrong input")


readint("Enter a number from -10 to 10",-10, 10)