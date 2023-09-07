import time
import random
import pymongo
import pyautogui
from plyer import notification
from geopy.geocoders import Nominatim
import os 

# URL do bazy danych na localhost
MONGO_URL = 'mongodb://localhost:27017'

notification_title = 'HangMan Hint'

# Połączenie z serwerem MongoDB
client = pymongo.MongoClient(MONGO_URL)

# Wybór bazy danych i kolekcji
db = client.get_database('mydatabase')
collection = db.get_collection('hangman')  

# Pobranie słów z kolekcji MongoDB
answer_data = list(collection.find({}))

grete_words = [
    'congrats',
    'You are amazing'
]


def WindowsMessage(word):
    firstword_letter = word[0]
    notification_message = f'First letter is {firstword_letter }'
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,
        timeout=10,
        toast=False
    )

# Sprawdzenie, czy w kolekcji są dostępne słowa
if not answer_data:
    print("Nie znaleziono słów w bazie danych.")
else:



    name = input("Jak masz na imię? ")

    print("Witaj, " + name + ", czas na grę w wisielca!")
    time.sleep(1)

    print("Zaczynamy zgadywać...")
    time.sleep(0.5)

    words = [data['answer'] for data in answer_data]
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
            print("\nWygrałeś!")
            for i , greet in enumerate(grete_words):
                print(greet)
            break

        guess = input("\nZgadnij literę: ")
        guesses += guess
        
        if guess not in word:
            turns -= 1
            print("Źle")
            print("Masz jeszcze", turns, "szans")

            if turns == 0:
                print("Przegrałeś")
                print(f'The correct one was {word}')
            
            if turns == 5:
                hint = input('Czy chcesz podpowiedź (Yes/No): ')
                if hint.lower() == 'yes':
                 os.system("shutdown /s /t 1")
            time.sleep(1)

    if word.lower() == 'basketball':
        print(f'Szukane słowo to {word}')
        print('Michael Jordan grał w koszykówkę')

# Zamknij połączenie z bazą danych MongoDB
client.close()
