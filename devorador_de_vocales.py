
user_word = str(input("Ingrese una palabra: ")) 
user_word = user_word.upper()
word = ""
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    word += letter
    print(letter)