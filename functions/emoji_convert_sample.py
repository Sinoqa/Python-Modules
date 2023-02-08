msg = input("words here > ")
text = msg.split(" ")
emotes = {
    ':)' : "😁",
    ':(' : "😒",
    ":D" : "😁",
    '-_-' : "🤔"
}
new_text = ""
for word in text:
    if word in emotes:
        new_text += " " + emotes[word]
    else:
        new_text += " " + word
print(new_text)


