def my_split(strng):
    new_string = []
    text = strng.split(" ")
    for word in text:
        if word != "":
            new_string.append(word)
    return new_string


print(my_split("To be or not to be, that  is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("    "))
print(my_split(" abc "))
print(my_split(""))

--end
