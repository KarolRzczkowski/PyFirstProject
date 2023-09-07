import time
import random
import pymongo
name = input("What's your name? ")

#url to localhost to database
MONGO_URL = 'mongodb://localhost:27017'

db = pymongo.db('mydatabse')

collection  = db.collection('')

print("Hello, " + name + ", Time to play Hangman!")
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

words = ["Basketball", "Pyjamas", "Python"]
word = random.choice(words)

guesses = ""
turns = 10

while turns > 0:
    failed = 0  

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou won!")
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You lose")

        if turns == 5:
            time(2)
            print("Did you lose?")
            time(0.5)
            print('no')    
        time(1)
if word == 'Basketball':
    print(f'The word was {word}')
    print('Micheal Jordan play bassketball')
