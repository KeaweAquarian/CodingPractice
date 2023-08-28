import random

def guess(x: int):
    guess = 0
   

    # number = random.randint(1, x)
    
    # while guess != number:
    #      guess = int(input("Geuss a number between 1 and 10?"))
    #      if guess == number:
    #          print("You win")
    #      else: 2
    #          print(f"{guess} is not quite right")

def comp_guess(x: int):
    com_guess = 0
    high = 300
    low = 1
    while com_guess != x:

        com_guess = random.randint(low,high)
        print(f"Computer guesses {com_guess}.")

        hint = input("If the geuss is too high enter \"h\" if it is too low enter \"l\", if it is correct enter \"w\".")

        match hint:
            case "h":
                high = com_guess-1
            case "l":
                low = com_guess+1
            case "w":
                print("Hurray I won")
                break
            case _:
                print("I didn't understand that responce.")

the_Number = input("What is your secret number?")
comp_guess(the_Number)
