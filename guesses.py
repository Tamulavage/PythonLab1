import random

ranNum = random.randint(1,10)
guessCount = 0
maxGuess = 10
guessRight = 0
guessedValues = []

print("Number is between 1 and 100!")

while guessCount < maxGuess and guessRight == 0:
    userGuess = input("Please guess a number: ")
    userGuess = int(userGuess)
    if not userGuess in guessedValues:
        guessedValues.append(userGuess)
        guessCount += 1
    if userGuess == ranNum:
        guessRight += 1
    elif userGuess > ranNum:
        print("You guessed to high")
    else:
        print("You guessed to low")

if guessRight == 1:
    print("You guessed right in ", guessCount, " guesses!")
else:
    print("You did not guess ", ranNum)
