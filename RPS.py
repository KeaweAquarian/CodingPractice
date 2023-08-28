import random
def play_rps():
    cont = True
    while cont:
        p_choice = input("Choose your type? For rock type r for paper type p for scissors type s!\n")
        c_choice = random.choice(['r','p','s'])
        print(f"Computer choise {c_choice}!")

        if p_choice == c_choice:
            print("It is a tie!")
        elif (p_choice == 'r' and c_choice == 's') or  (p_choice == 'p' and c_choice == 'r') or  (p_choice == 's' and c_choice == 'p'):
            print("Congradulation you win!")
        else: print("The computer wins!")

        play = input("Play again? y/n ")
        if (play != 'y'): cont = False


play_rps()