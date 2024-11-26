import random

words = ["pointer", "syntax", "array", "binary", "recursion", "iterate", "compile", "variable", "function", "algorithm"]
flag = False
count = 0
word = random.choice(words)
guess = ['_'] * len(word)
wrong = []
while count < 7 and (list(word) != guess):
    
    print("HANGMAN\n")
    for i in range(count):
        print(" ", end="")
    print("^")    
    char = input("Your guess:\n")
    indices = []
    found = 0
    for i in range(len(word)):
        if char == word[i]:
            found = 1
            indices.append(i)

    if found == 1:
        for i in indices:
            guess[i] = char
    else:
        count += 1
        wrong.append(char)

    wrongstr = ''.join(wrong)
    guessstr = ''.join(guess)
    print("WRONG GUESSES: " + wrongstr + "\n")
    print("THE WORD: " + guessstr + "\n")

if count == 7:
    print(word)
    print("YOU ARE HANGED\n")
else:
    print("PHEW...YOU ARE SAVED\n")
