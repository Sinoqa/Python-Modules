status = False
while status != True:
    def readint(prompt, min, max):
        try:
            while prompt != int:
                if prompt < min or prompt > max:
                    print(f"Error: The value is not within permitted range {min}..{max}")
        except ValueError:
            print("error")

number = int(input(f"Enter a number from -10 to 10 "))
v = readint(number, -10, 10)


