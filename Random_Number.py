import random

def guess(x: int):
    guess = 0
   

    number = random.randint(1, x)
    
    while guess != number:
         guess = int(input("Geuss a number between 1 and 10?"))
         if guess == number:
             print("You win")
         else: 2
             print(f"{guess} is not quite right")


guess(10)
