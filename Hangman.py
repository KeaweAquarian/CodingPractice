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
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    i = 5
    while (i) > 0:
        print("You have used these letters " , ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter \n".lower())
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: i -=1

        elif user_letter in used_letters:
            print("You have already guessed that letter!\n")    
        else:
             print("I didn't understand that responce.\n") 
    if i == 0:
        print(f"Good try, but you have run out of chances. The word was {word}\n")   

hangman()



