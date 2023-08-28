import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()



print("Thank you for playing hangman. the computer has chossen the name of a member of your family. You can guess the letters of their name, \n \
      If you guess wrong more than 5 times you hang! Good luck.")

def hangman():
    word = list(get_valid_word)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters " , ''.join(used_letters))


guess = input("What letter do you choose?")



