letters = "abcdefghijklmneopqrstuvwxyz"

user = input("> ")
offset = int(input(">"))
cipher = ""
for letter in user:
    num = letters.find(letter.lower())
    if num + offset >= len(letters):
        num= +offset - len(letters)
    elif:
        num=+ offset
    return num


print(num)
